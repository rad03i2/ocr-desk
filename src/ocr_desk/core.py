from __future__ import annotations

import json
import shutil
import subprocess
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Callable, Sequence

SUPPORTED_INPUTS = {".png", ".jpg", ".jpeg", ".tif", ".tiff", ".bmp", ".webp"}
FORMATS = {"txt", "tsv", "hocr", "pdf"}


class OcrError(RuntimeError):
    """User-facing OCR failure."""


@dataclass(frozen=True)
class OcrResult:
    input: str
    output: str
    language: str
    format: str

    def to_json(self) -> str:
        return json.dumps(asdict(self), ensure_ascii=False)


def find_tesseract(explicit: str | None = None) -> str:
    if explicit:
        path = Path(explicit).expanduser()
        if not path.is_file():
            raise OcrError(f"Tesseract executable not found: {path}")
        return str(path)
    found = shutil.which("tesseract")
    if not found:
        raise OcrError("Tesseract was not found in PATH. Install it or pass --tesseract PATH.")
    return found


def validate_input(path: Path) -> Path:
    path = path.expanduser().resolve()
    if not path.is_file():
        raise OcrError(f"Input file does not exist: {path}")
    if path.suffix.lower() not in SUPPORTED_INPUTS:
        raise OcrError(f"Unsupported input type: {path.suffix or '(none)'}")
    return path


def build_command(executable: str, source: Path, output_base: Path, language: str,
                  fmt: str, psm: int, oem: int) -> list[str]:
    if fmt not in FORMATS:
        raise OcrError(f"Unsupported output format: {fmt}")
    if not 0 <= psm <= 13:
        raise OcrError("--psm must be between 0 and 13")
    if not 0 <= oem <= 3:
        raise OcrError("--oem must be between 0 and 3")
    if not language or any(c.isspace() for c in language):
        raise OcrError("Language must be a Tesseract code such as eng, ara, or ara+eng")
    cmd = [executable, str(source), str(output_base), "-l", language, "--psm", str(psm), "--oem", str(oem)]
    if fmt != "txt":
        cmd.append(fmt)
    return cmd


def recognize(source: str | Path, output: str | Path | None = None, *, language: str = "eng",
              fmt: str = "txt", psm: int = 3, oem: int = 3, overwrite: bool = False,
              tesseract: str | None = None,
              runner: Callable[..., subprocess.CompletedProcess[str]] = subprocess.run) -> OcrResult:
    src = validate_input(Path(source))
    executable = find_tesseract(tesseract)
    suffix = ".html" if fmt == "hocr" else f".{fmt}"
    target = Path(output).expanduser().resolve() if output else src.with_name(src.stem + ".ocr" + suffix)
    if target == src:
        raise OcrError("Output must not overwrite the source image")
    if target.exists() and not overwrite:
        raise OcrError(f"Output already exists: {target}. Use --overwrite to replace it.")
    target.parent.mkdir(parents=True, exist_ok=True)
    # Tesseract appends the renderer extension; use a temporary base to avoid partial final files.
    temp_base = target.parent / ("." + target.name + ".ocrdesk-tmp")
    generated = Path(str(temp_base) + suffix)
    generated.unlink(missing_ok=True)
    cmd = build_command(executable, src, temp_base, language, fmt, psm, oem)
    try:
        proc = runner(cmd, text=True, capture_output=True, check=False)
    except OSError as exc:
        raise OcrError(f"Could not start Tesseract: {exc}") from exc
    if proc.returncode != 0:
        generated.unlink(missing_ok=True)
        detail = (proc.stderr or proc.stdout or "unknown Tesseract error").strip()
        raise OcrError(f"Tesseract failed ({proc.returncode}): {detail}")
    if not generated.is_file():
        raise OcrError(f"Tesseract completed without producing {generated.name}")
    if overwrite:
        target.unlink(missing_ok=True)
    generated.replace(target)
    return OcrResult(str(src), str(target), language, fmt)


def list_languages(tesseract: str | None = None,
                   runner: Callable[..., subprocess.CompletedProcess[str]] = subprocess.run) -> Sequence[str]:
    executable = find_tesseract(tesseract)
    proc = runner([executable, "--list-langs"], text=True, capture_output=True, check=False)
    if proc.returncode != 0:
        raise OcrError((proc.stderr or "Unable to list languages").strip())
    lines = [line.strip() for line in proc.stdout.splitlines() if line.strip()]
    return [line for line in lines if not line.lower().startswith("list of available languages")]
