<div align="center">

# OCR Desk

**أداة محلية بسيطة وموثوقة لاستخراج النصوص من الصور وإنشاء ملفات قابلة للبحث**  
**A dependable local-first OCR command-line tool powered by Tesseract**

[![CI](https://github.com/rad03i2/ocr-desk/actions/workflows/ci.yml/badge.svg)](https://github.com/rad03i2/ocr-desk/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Privacy](https://img.shields.io/badge/Privacy-Local--First-blue)
![Version](https://img.shields.io/badge/Version-1.0.0-informational)

[العربية](#-العربية) · [English](#-english)

</div>

---

<h2 dir="rtl">🇮🇶 العربية</h2>

<h3 dir="rtl">نظرة سريعة</h3>

<p dir="rtl">
أداة سطر أوامر لمعالجة صور المستندات واستخراج النصوص منها محليًا على جهازك، من دون رفع الملفات إلى خدمات خارجية. صُممت لتوفير طريقة ثابتة وآمنة لتنفيذ مهام التعرّف الضوئي على النصوص، مع حماية ملفات المصدر والإخراج وإمكانية استخدامها داخل السكربتات وعمليات الأتمتة.
</p>

<p dir="rtl">
المشروع يعتمد على محرك <strong>تيسراكت</strong> المثبّت على الجهاز، ويضيف فوقه واجهة أوامر واضحة، والتحقق من المدخلات، وإدارة آمنة للنتائج، واختبارات آلية لضمان سلوك متوقع وقابل للتكرار.
</p>

<h3 dir="rtl">✨ أبرز المزايا</h3>

<ul dir="rtl">
  <li>معالجة الصور محليًا بالكامل للحفاظ على الخصوصية.</li>
  <li>استخراج النصوص العادية أو إنشاء ملفات قابلة للبحث.</li>
  <li>دعم لغة واحدة أو عدة لغات في عملية التعرّف نفسها.</li>
  <li>دعم اللغة العربية والإنجليزية عند تثبيت حزم اللغات المناسبة.</li>
  <li>إتاحة التحكم في طريقة تحليل الصفحة ومحرك التعرّف.</li>
  <li>عرض اللغات المثبّتة والمتاحة على الجهاز.</li>
  <li>إرجاع نتائج منظمة مناسبة للسكربتات والأتمتة.</li>
  <li>منع استبدال الصورة الأصلية أو الملفات الموجودة عن طريق الخطأ.</li>
  <li>إنشاء الناتج في ملف مؤقت قبل اعتماد الملف النهائي.</li>
  <li>لا حسابات، ولا مفاتيح وصول، ولا تتبع، ولا رفع للمستندات.</li>
</ul>

<p dir="rtl"><strong>صيغ الصور المدعومة:</strong></p>

```text
PNG · JPEG · TIFF · BMP · WebP
```

<p dir="rtl"><strong>صيغ الإخراج:</strong></p>

```text
TXT · TSV · hOCR · Searchable PDF
```

<h3 dir="rtl">⚙️ المتطلبات</h3>

<ul dir="rtl">
  <li>بايثون إصدار 3.10 أو أحدث.</li>
  <li>تثبيت محرك تيسراكت على الجهاز.</li>
  <li>تثبيت حزم اللغات التي تحتاجها، مثل العربية أو الإنجليزية.</li>
</ul>

<p dir="rtl">
المحرك نفسه غير مضمّن داخل المستودع، لذلك يجب تثبيته بصورة مستقلة قبل تشغيل المشروع.
</p>

```bash
tesseract --version
```

<h3 dir="rtl">🚀 التثبيت</h3>

```bash
git clone https://github.com/rad03i2/ocr-desk.git
cd ocr-desk
python -m pip install -e .
ocr-desk --version
```

<h3 dir="rtl">🧪 أمثلة الاستخدام</h3>

<p dir="rtl"><strong>استخراج النص من صورة بالإعدادات الافتراضية:</strong></p>

```bash
ocr-desk scan scan.png
```

<p dir="rtl"><strong>استخراج نص عربي وإنجليزي وحفظه في ملف:</strong></p>

```bash
ocr-desk scan document.jpg -l ara+eng -o document.txt
```

<p dir="rtl"><strong>إنشاء ملف قابل للبحث من صورة عربية:</strong></p>

```bash
ocr-desk scan page.tif -l ara -f pdf -o page-searchable.pdf
```

<p dir="rtl"><strong>عرض اللغات المثبّتة:</strong></p>

```bash
ocr-desk languages
```

<p dir="rtl"><strong>تغيير طريقة تحليل الصفحة وإرجاع بيانات منظمة:</strong></p>

```bash
ocr-desk scan page.png --psm 6 --json
```

<p dir="rtl"><strong>على ويندوز، عند عدم اكتشاف المحرك تلقائيًا:</strong></p>

```powershell
ocr-desk --tesseract "C:\Program Files\Tesseract-OCR\tesseract.exe" scan page.png -l ara
```

<h3 dir="rtl">🧩 خيارات مهمة</h3>

| الخيار | وظيفته |
|---|---|
| `-l` | تحديد اللغة أو اللغات المستخدمة في التعرّف |
| `-o` | تحديد اسم ومسار ملف الإخراج |
| `-f` | اختيار صيغة الإخراج |
| `--psm` | تحديد طريقة تقسيم الصفحة |
| `--oem` | تحديد نمط محرك التعرّف |
| `--json` | إرجاع معلومات النتيجة بصيغة منظمة |
| `--overwrite` | السماح باستبدال ملف إخراج موجود عند الحاجة |
| `--tesseract` | تحديد المسار اليدوي للملف التنفيذي للمحرك |

<h3 dir="rtl">🔐 الخصوصية والأمان</h3>

<p dir="rtl">
كل عمليات التعرّف تتم على الجهاز من خلال المحرك المحلي. لا يقوم المشروع بإرسال الصور أو النصوص المستخرجة عبر الشبكة، كما لا يعدّل الصورة الأصلية. ومع ذلك، قد تحتوي الملفات الناتجة على معلومات حساسة، لذلك يُنصح بحمايتها وعدم تمرير النص المستخرج مباشرة إلى أوامر النظام أو عمليات آلية قبل التحقق منه.
</p>

<p dir="rtl">
للتفاصيل الإضافية راجع ملف <a href="SECURITY.md">سياسة الأمان</a>.
</p>

<h3 dir="rtl">📁 بنية المشروع</h3>

```text
ocr-desk/
├── src/ocr_desk/
│   ├── cli.py          # واجهة الأوامر ورموز الخروج
│   └── core.py         # التحقق وبناء الأوامر وإدارة الإخراج الآمن
├── tests/
│   └── test_core.py    # الاختبارات الأساسية
├── .github/workflows/  # التكامل المستمر
├── CONTRIBUTING.md
├── SECURITY.md
├── LICENSE
└── pyproject.toml
```

<h3 dir="rtl">✅ الاختبارات</h3>

```bash
python -m unittest discover -s tests -v
```

<p dir="rtl">
لا تتطلب الاختبارات وجود المحرك فعليًا في جميع الحالات، لأن عملية التنفيذ تُحاكى عند الحاجة. كما يعمل التكامل المستمر على عدة أنظمة تشغيل وإصدارات مختلفة من بايثون.
</p>

<h3 dir="rtl">📌 حدود الإصدار الحالي</h3>

<ul dir="rtl">
  <li>جودة التعرّف تعتمد على جودة الصورة واتجاهها وتخطيطها وحزمة اللغة المستخدمة.</li>
  <li>الإصدار الحالي يستقبل الصور مباشرة ولا يستقبل ملفات المستندات متعددة الصفحات كمدخل.</li>
  <li>لا توجد حاليًا معالجة مسبقة تلقائية لإزالة التشويش أو تصحيح الميل أو الدوران أو القص.</li>
  <li>لا توجد واجهة رسومية أو معالجة مجلد كامل في الإصدار الحالي.</li>
</ul>

<h3 dir="rtl">🗺️ أفكار التطوير المستقبلية</h3>

<ul dir="rtl">
  <li>المعالجة الجماعية لعدة صور دفعة واحدة.</li>
  <li>تحسين الصور اختياريًا قبل التعرّف.</li>
  <li>إضافة واجهة سطح مكتب خفيفة.</li>
</ul>

<h3 dir="rtl">🤝 المساهمة</h3>

<p dir="rtl">
المساهمات مرحب بها. راجع ملف <a href="CONTRIBUTING.md">دليل المساهمة</a> قبل إرسال التعديلات، وحافظ على بساطة المشروع وخصوصيته وقابليته للاختبار.
</p>

<h3 dir="rtl">📄 الترخيص</h3>

<p dir="rtl">
المشروع متاح بموجب ترخيص MIT. راجع ملف <a href="LICENSE">LICENSE</a>.
</p>

<h3 dir="rtl">👤 المطوّر</h3>

<p dir="rtl">
<strong>رضوان عبدالهادي أحمد</strong><br>
حساب GitHub: <a href="https://github.com/rad03i2">@rad03i2</a>
</p>

---

## 🇬🇧 English

### Overview

OCR Desk is a small, dependable, local-first command-line workspace for turning scanned images into searchable text or documents with Tesseract OCR. It provides a predictable CLI, input validation, safe output handling, machine-readable results, and automated tests without uploading documents to a cloud service.

### Why OCR Desk?

Tesseract is powerful, but renderer syntax, language selection, and output naming can become awkward inside scripts. OCR Desk provides one stable command for common OCR jobs while keeping the recognition engine transparent and replaceable.

### Features

- Recognize PNG, JPEG, TIFF, BMP, and WebP images.
- Output plain text, TSV, hOCR, or searchable PDF.
- Select one or multiple installed languages such as `eng`, `ara`, or `ara+eng`.
- Control Tesseract page segmentation with `--psm` and engine mode with `--oem`.
- Discover installed language packs with `ocr-desk languages`.
- Produce JSON results for scripts and automation.
- Select an explicit Tesseract executable when it is not available on `PATH`.
- Refuse accidental source replacement and existing-output replacement by default.
- Write renderer output to a temporary location before promoting the completed file.
- No telemetry, accounts, API keys, or document uploads.

### Requirements

- Python 3.10+
- Tesseract OCR installed locally
- Any language packs required for your documents

Tesseract is intentionally not bundled with this repository.

```bash
tesseract --version
```

### Installation

```bash
git clone https://github.com/rad03i2/ocr-desk.git
cd ocr-desk
python -m pip install -e .
ocr-desk --version
```

### Usage

Extract text with the default settings:

```bash
ocr-desk scan scan.png
```

Arabic and English to a chosen output file:

```bash
ocr-desk scan receipt.jpg -l ara+eng -o receipt.txt
```

Create a searchable PDF:

```bash
ocr-desk scan page.tif -l eng -f pdf -o page-searchable.pdf
```

Tune segmentation and request JSON metadata:

```bash
ocr-desk scan page.png --psm 6 --json
```

List installed languages:

```bash
ocr-desk languages
```

On Windows, if Tesseract is not available on `PATH`:

```powershell
ocr-desk --tesseract "C:\Program Files\Tesseract-OCR\tesseract.exe" scan page.png -l ara
```

Use `--overwrite` only when replacing an existing output is intentional.

### Project structure

```text
src/ocr_desk/core.py   validation, command construction, safe output workflow
src/ocr_desk/cli.py    command-line interface and exit codes
tests/test_core.py     unit/integration-style wrapper tests
.github/workflows/     cross-platform CI
```

### Testing

```bash
python -m unittest discover -s tests -v
```

The test suite can simulate execution where appropriate, so it does not require Tesseract for every test. CI validates installation, tests, and CLI behavior across multiple operating systems and Python versions.

### Security & privacy

Recognition happens locally through the selected Tesseract executable. OCR Desk itself performs no document uploads and does not modify the source image. OCR output may still contain sensitive information, so protect generated files and treat recognized text as untrusted before feeding it into shell commands or other automated systems. See [SECURITY.md](SECURITY.md).

### Current limitations

- OCR quality depends on Tesseract, language data, image quality, orientation, and layout.
- This release accepts image formats supported by Tesseract; PDF input is not supported directly.
- Automatic preprocessing, deskewing, denoising, rotation, and cropping are not included yet.
- A desktop GUI and batch-directory mode are not included in the current release.
- hOCR is produced by Tesseract with an `.html` output filename.

### Roadmap

Possible future additions include batch processing, opt-in image preprocessing, and a lightweight desktop interface.

### Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Keep changes testable, local-first, and documented.

### License

MIT License — see [LICENSE](LICENSE).

### Author

**Radwan Abdulhadi Ahmed**  
**رضوان عبدالهادي أحمد**  
GitHub: **[@rad03i2](https://github.com/rad03i2)**

---

<div align="center">

Built with a focus on **privacy · reliability · simplicity**

</div>
