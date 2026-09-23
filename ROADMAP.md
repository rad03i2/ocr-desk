<div align="center">

# 🧭 OCR Desk Roadmap

### A focused path from reliable CLI to a richer local OCR workspace

**Built by Radwan Abdulhadi Ahmed · @rad03i2**

</div>

---

## ✅ Current foundation — v1.0

- Local-first OCR through an installed Tesseract engine.
- PNG, JPEG, TIFF, BMP, and WebP input.
- TXT, TSV, hOCR, and searchable PDF output.
- Arabic, English, and multi-language recognition when language packs are installed.
- Page segmentation and OCR engine mode controls.
- JSON output for scripts and automation.
- Safe output handling and overwrite protection.
- Cross-platform automated tests on Windows, Ubuntu, and macOS.
- Arabic and English documentation.

## 🔵 Next — usability

These are intended improvements, not features of the current release.

- Batch-directory processing.
- Progress reporting for long jobs.
- Friendlier language-pack diagnostics.
- Clearer command presets for common document layouts.
- Optional output naming templates.

## 🟣 Later — image preparation

- Opt-in rotation and orientation helpers.
- Deskew support.
- Denoising and contrast preparation.
- Crop helpers for scanned pages.
- Preview-before-processing workflow.

## ✨ Future — desktop experience

- Lightweight desktop interface while preserving the CLI.
- Drag-and-drop document workflow.
- Visual language and output selection.
- Batch queue with per-file status.
- Local history with privacy-first defaults.

## Design principles

Every future feature should preserve these rules:

1. **Local first** — documents stay on the user's machine unless the user explicitly chooses otherwise.
2. **Predictable** — command behavior and output paths should be easy to understand.
3. **Safe by default** — avoid destructive file operations and silent replacement.
4. **Scriptable** — the CLI remains useful for automation even if a GUI is added.
5. **Documented** — user-facing changes should be reflected in both Arabic and English documentation.

---

<div align="center">

**Rad03i2 · Simple tools. Real impact.**

</div>
