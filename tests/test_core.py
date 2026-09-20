import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from ocr_desk.core import OcrError, build_command, recognize


class CoreTests(unittest.TestCase):
    def test_build_command_for_arabic_pdf(self):
        cmd = build_command("tesseract", Path("a.png"), Path("out"), "ara+eng", "pdf", 6, 3)
        self.assertEqual(cmd[-1], "pdf")
        self.assertIn("ara+eng", cmd)

    def test_invalid_psm_is_rejected(self):
        with self.assertRaises(OcrError):
            build_command("tesseract", Path("a.png"), Path("out"), "eng", "txt", 99, 3)

    def test_unsupported_input_is_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            source = Path(td) / "notes.docx"
            source.write_bytes(b"x")
            with self.assertRaises(OcrError):
                recognize(source, tesseract=sys.executable)

    def test_recognize_promotes_temp_output(self):
        with tempfile.TemporaryDirectory() as td:
            source = Path(td) / "scan.png"
            source.write_bytes(b"not decoded by wrapper")
            target = Path(td) / "result.txt"
            def fake(cmd, **kwargs):
                Path(cmd[2] + ".txt").write_text("hello OCR", encoding="utf-8")
                return subprocess.CompletedProcess(cmd, 0, "", "")
            result = recognize(source, target, tesseract=sys.executable, runner=fake)
            self.assertEqual(target.read_text(encoding="utf-8"), "hello OCR")
            self.assertEqual(result.format, "txt")

    def test_existing_output_requires_overwrite(self):
        with tempfile.TemporaryDirectory() as td:
            source = Path(td) / "scan.jpg"
            target = Path(td) / "result.txt"
            source.write_bytes(b"x")
            target.write_text("keep", encoding="utf-8")
            with self.assertRaises(OcrError):
                recognize(source, target, tesseract=sys.executable)
            self.assertEqual(target.read_text(encoding="utf-8"), "keep")


if __name__ == "__main__":
    unittest.main()
