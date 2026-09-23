# OCR Desk — English Guide

**A dependable local-first command-line tool for extracting text from images and creating searchable documents with Tesseract.**

[Back to the main page](README.md)

---

## What is OCR Desk?

OCR Desk is a local command-line workspace for repeatable OCR tasks. It wraps an installed Tesseract engine with predictable commands, input validation, safer output handling, and automation-friendly results.

The project is designed for users who want OCR without uploading documents to a cloud service.

## Why use it?

- Extract text from scans and document images.
- Work with Arabic, English, or multiple installed languages.
- Create searchable PDF output from image input.
- Use OCR in scripts and automation workflows.
- Keep source documents on the local machine.
- Avoid accidental source or output replacement.

## Key features

- Local-first document processing.
- PNG, JPEG, TIFF, BMP, and WebP input.
- TXT, TSV, hOCR, and searchable PDF output.
- One or multiple installed recognition languages.
- Page segmentation and engine-mode controls.
- Installed-language discovery.
- Structured JSON result output.
- Explicit Tesseract executable selection.
- Safe temporary-output workflow.
- No telemetry, accounts, API keys, or document uploads.

## Requirements

- Python 3.10+
- Tesseract OCR installed locally
- Any language packs required by your documents

Verify Tesseract first:

```bash
tesseract --version
```

## Installation

```bash
git clone https://github.com/rad03i2/ocr-desk.git
cd ocr-desk
python -m pip install -e .
ocr-desk --version
```

## Quick start

Extract text:

```bash
ocr-desk scan scan.png
```

Arabic and English recognition:

```bash
ocr-desk scan document.jpg -l ara+eng -o document.txt
```

Create a searchable PDF:

```bash
ocr-desk scan page.tif -l eng -f pdf -o page-searchable.pdf
```

List installed languages:

```bash
ocr-desk languages
```

Request structured result metadata:

```bash
ocr-desk scan page.png --psm 6 --json
```

On Windows, when Tesseract is not on `PATH`:

```powershell
ocr-desk --tesseract "C:\Program Files\Tesseract-OCR\tesseract.exe" scan page.png -l ara
```

## Safe output behavior

OCR Desk refuses to overwrite an existing output by default. Use the following option only when replacement is intentional:

```text
--overwrite
```

The source image is not intentionally modified.

## Privacy

Recognition happens through the locally selected Tesseract executable. OCR Desk itself does not upload source images or OCR results and does not require an account or API key.

Generated OCR text may still contain sensitive information, so protect the output as you would protect the original document.

## Project structure

```text
src/ocr_desk/core.py    validation, command construction, safe output workflow
src/ocr_desk/cli.py     command-line interface and exit codes
tests/test_core.py      behavioral tests
.github/workflows/      continuous integration configuration
```

## Testing

```bash
python -m unittest discover -s tests -v
```

The test suite can simulate execution where appropriate, so a live Tesseract process is not required for every test.

Continuous integration covers Ubuntu, Windows, and macOS on multiple supported Python versions.

## Current limitations

- OCR accuracy depends on Tesseract, installed language data, image quality, orientation, and layout.
- The current release accepts image input rather than PDF documents as input.
- Image preprocessing such as deskewing, denoising, rotation, and cropping is not included yet.
- There is no desktop GUI in the current release.
- Batch-directory processing is not included yet.

## Possible future work

- Batch processing.
- Optional image preprocessing.
- A lightweight desktop interface.
- Additional document workflow helpers.

## Project documents

- [Security policy](SECURITY.md)
- [Contributing guide](CONTRIBUTING.md)
- [Changelog](CHANGELOG.md)
- [License](LICENSE)

## Author

**Radwan Abdulhadi Ahmed**  
**رضوان عبدالهادي أحمد**  
GitHub: **@rad03i2**
