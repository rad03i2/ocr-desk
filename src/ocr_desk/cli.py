from __future__ import annotations

import argparse
import json
import sys
from . import __version__
from .core import FORMATS, OcrError, list_languages, recognize


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="ocr-desk", description="Private, local OCR workflows powered by Tesseract.")
    p.add_argument("--version", action="version", version=f"OCR Desk {__version__}")
    p.add_argument("--tesseract", help="Path to the Tesseract executable")
    sub = p.add_subparsers(dest="command", required=True)
    scan = sub.add_parser("scan", help="Recognize text from an image")
    scan.add_argument("input")
    scan.add_argument("-o", "--output")
    scan.add_argument("-l", "--language", default="eng", help="Tesseract language(s), e.g. ara+eng")
    scan.add_argument("-f", "--format", choices=sorted(FORMATS), default="txt")
    scan.add_argument("--psm", type=int, default=3, help="Page segmentation mode (0-13)")
    scan.add_argument("--oem", type=int, default=3, help="OCR engine mode (0-3)")
    scan.add_argument("--overwrite", action="store_true")
    scan.add_argument("--json", action="store_true", dest="as_json")
    sub.add_parser("languages", help="List installed Tesseract language packs")
    return p


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    try:
        if args.command == "languages":
            langs = list_languages(args.tesseract)
            print("\n".join(langs))
            return 0
        result = recognize(args.input, args.output, language=args.language, fmt=args.format,
                           psm=args.psm, oem=args.oem, overwrite=args.overwrite,
                           tesseract=args.tesseract)
        if args.as_json:
            print(result.to_json())
        else:
            print(f"OCR complete: {result.output}")
        return 0
    except OcrError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
