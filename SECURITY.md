# Security Policy

## Scope
OCR Desk runs locally and sends no document or OCR content over the network. It invokes the Tesseract executable selected by the user or discovered on `PATH`.

## Safe use
- Install Tesseract from a trusted operating-system package or the official project guidance.
- Treat OCR output as untrusted text before passing it to shells, templates, databases, or automation.
- OCR Desk refuses to replace an existing output unless `--overwrite` is explicitly supplied.
- The source image is never intentionally modified.

## Reporting
Please open a GitHub issue with a minimal reproduction that contains no confidential documents. For sensitive reports, avoid posting private data publicly and use GitHub's private vulnerability reporting if it is enabled for this repository.

Maintainer: Radwan Abdulhadi Ahmed (@rad03i2)
