<div align="center">

# 🧩 OCR Desk Architecture

### Small surface. Clear responsibilities. Local execution.

</div>

## Overview

OCR Desk intentionally keeps its architecture compact. The command-line layer parses user intent, while the core layer validates inputs, builds the Tesseract invocation, executes recognition, and protects output handling.

```text
User command
    │
    ▼
┌─────────────────────┐
│  CLI / argparse     │
│  src/ocr_desk/cli.py│
└─────────┬───────────┘
          │ validated options
          ▼
┌─────────────────────┐
│   OCR core          │
│  validation         │
│  command building   │
│  output workflow    │
└─────────┬───────────┘
          │ subprocess
          ▼
┌─────────────────────┐
│ Tesseract executable│
│ installed locally   │
└─────────┬───────────┘
          │ generated output
          ▼
┌─────────────────────┐
│ Safe final output   │
└─────────────────────┘
```

## Main components

### `src/ocr_desk/cli.py`

Responsible for:

- top-level commands and options;
- input parsing;
- version output;
- language-list command;
- human-readable or JSON completion output;
- mapping controlled OCR errors to a non-zero exit code.

### `src/ocr_desk/core.py`

Responsible for:

- validating input and output paths;
- supported-format handling;
- selecting or locating Tesseract;
- building the recognition command;
- executing recognition;
- preventing accidental replacement;
- managing temporary renderer output before promotion to the final result.

### `tests/`

Covers core behavior without requiring a real Tesseract installation for the simulated execution paths used by the test suite.

### `.github/workflows/ci.yml`

Runs installation, tests, and a CLI smoke test across multiple Python versions on Ubuntu, Windows, and macOS.

## Privacy boundary

OCR Desk itself does not need a remote OCR API. Recognition is delegated to the locally selected Tesseract executable. This keeps the project architecture useful for privacy-sensitive workflows while still allowing scripts and automation to consume results.

## Design constraints

- Avoid hidden network dependencies in the OCR path.
- Keep destructive behavior opt-in.
- Keep the core usable independently of future GUI work.
- Preserve stable CLI behavior where possible.
- Prefer explicit configuration over surprising implicit state.

---

<div align="center">

**OCR Desk · a Rad03i2 project**

</div>
