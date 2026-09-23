<div align="center">

<img src="assets/ocr-desk-brand-cover.svg" alt="OCR Desk — Radwan Abdulhadi Ahmed" width="100%" />

# OCR Desk

### Local-first OCR for reliable document workflows

**استخراج النصوص من الصور محليًا — ببساطة، خصوصية، ونتائج قابلة للأتمتة**

[![CI](https://github.com/rad03i2/ocr-desk/actions/workflows/ci.yml/badge.svg)](https://github.com/rad03i2/ocr-desk/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Version](https://img.shields.io/badge/Version-1.0.0-informational)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Privacy](https://img.shields.io/badge/Privacy-Local--First-blue)

**[العربية](README_AR.md) · [English](README_EN.md) · [Changelog](CHANGELOG.md) · [Security](SECURITY.md)**

</div>

---

<div dir="rtl" align="right">

## 🇮🇶 نبذة سريعة

**OCR Desk** أداة خفيفة تعمل محليًا على جهازك لاستخراج النصوص من صور المستندات وإنشاء ملفات قابلة للبحث. صُممت لمن يريد طريقة واضحة وآمنة للتعرّف على النصوص من دون رفع المستندات إلى خدمة سحابية.

### لماذا هذا المشروع؟

- يحافظ على المستندات داخل جهاز المستخدم.
- يدعم العربية والإنجليزية ولغات أخرى عند تثبيت حزمها.
- يحمي الصورة الأصلية من التعديل غير المقصود.
- يمنع استبدال ملفات الإخراج الموجودة بصورة افتراضية.
- يصلح للاستخدام اليدوي أو داخل السكربتات والأتمتة.
- يعمل عبر أنظمة تشغيل متعددة ويخضع لاختبارات آلية.

### صيغ الإدخال والإخراج

</div>

<div align="center">

| Input | Output |
|:---:|:---:|
| PNG · JPEG · TIFF · BMP · WebP | TXT · TSV · hOCR · Searchable PDF |

</div>

<div dir="rtl" align="right">

### تشغيل سريع

</div>

```bash
git clone https://github.com/rad03i2/ocr-desk.git
cd ocr-desk
python -m pip install -e .
ocr-desk --version
```

<div dir="rtl" align="right">

استخراج نص عربي وإنجليزي من صورة:

</div>

```bash
ocr-desk scan document.jpg -l ara+eng -o document.txt
```

<div dir="rtl" align="right">

إنشاء ملف قابل للبحث:

</div>

```bash
ocr-desk scan page.tif -l ara -f pdf -o page-searchable.pdf
```

<div dir="rtl" align="right">

### الخصوصية أولًا

المعالجة تتم على جهازك من خلال محرك التعرّف المثبّت محليًا. المشروع نفسه لا يحتاج إلى حساب مستخدم أو مفتاح وصول، ولا يرسل المستندات إلى خدمة خارجية.

> **للدليل العربي الكامل:** [README_AR.md](README_AR.md)

</div>

---

## 🇬🇧 English overview

OCR Desk is a dependable local-first command-line workspace for extracting text from document images and producing searchable output through an installed Tesseract engine.

### Highlights

- Local document processing with no OCR uploads performed by the project.
- Arabic, English, and multi-language recognition.
- TXT, TSV, hOCR, and searchable PDF output.
- Safe output handling and source-file protection.
- JSON results for scripts and automation.
- Cross-platform automated testing.

Quick example:

```bash
ocr-desk scan receipt.jpg -l ara+eng -o receipt.txt
```

> **Full English guide:** [README_EN.md](README_EN.md)

---

## Project status

| Area | Status |
|---|---|
| Core CLI | ✅ Ready |
| Automated tests | ✅ Included |
| Cross-platform CI | ✅ Included |
| Arabic documentation | ✅ Included |
| English documentation | ✅ Included |
| Local-first privacy | ✅ Included |
| Desktop GUI | 🔭 Future |
| Batch directory mode | 🔭 Future |
| Image preprocessing | 🔭 Future |

## Repository map

```text
ocr-desk/
├── assets/                # Branded visual identity
├── src/ocr_desk/          # Application source
├── tests/                 # Automated tests
├── .github/workflows/     # Cross-platform CI
├── README_AR.md           # الدليل العربي الكامل
├── README_EN.md           # Full English guide
├── CONTRIBUTING.md        # Contribution guide
├── SECURITY.md            # Security policy
├── CHANGELOG.md           # Release history
└── LICENSE                # MIT License
```

## Documentation

- 🇮🇶 [الدليل العربي الكامل](README_AR.md)
- 🇬🇧 [Full English guide](README_EN.md)
- 🧪 [Contributing](CONTRIBUTING.md)
- 🔐 [Security policy](SECURITY.md)
- 📝 [Changelog](CHANGELOG.md)
- 📄 [MIT License](LICENSE)

---

<div align="center">

### Developed by Radwan Abdulhadi Ahmed

**رضوان عبدالهادي أحمد** · **@rad03i2**

Built with a focus on reliability, privacy, and clear documentation.

</div>
