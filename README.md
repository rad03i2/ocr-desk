# OCR Desk

A small, dependable, local-first command-line workspace for turning scanned images into searchable text or documents with Tesseract OCR.

**Author:** Radwan Abdulhadi Ahmed · **GitHub:** @rad03i2

## English

### Overview
OCR Desk wraps the installed Tesseract engine with a predictable CLI, validation, safe output handling, machine-readable results, and automated tests. It is useful when you want repeatable OCR without uploading documents to a cloud service.

### Why it exists
Tesseract is powerful, but its renderer syntax and output naming are easy to get wrong in scripts. OCR Desk provides one stable command for common OCR jobs while keeping the actual recognition engine transparent and replaceable.

### Features
- Recognize PNG, JPEG, TIFF, BMP, and WebP images.
- Output plain text (`txt`), TSV, hOCR, or searchable PDF.
- Select one or multiple installed languages such as `eng`, `ara`, or `ara+eng`.
- Control Tesseract page segmentation (`--psm`) and engine mode (`--oem`).
- Discover installed language packs with `ocr-desk languages`.
- JSON result output for scripts and automation.
- Explicit Tesseract executable selection for machines where it is not on `PATH`.
- Refuses accidental source replacement and existing-output replacement by default.
- Uses a temporary renderer output before promoting the completed file.
- No telemetry, accounts, API keys, or document uploads.

### Requirements
- Python 3.10+
- Tesseract OCR installed locally, including the language packs you need

Tesseract itself is intentionally not bundled. Verify it first with `tesseract --version`.

### Installation
```bash
git clone https://github.com/rad03i2/ocr-desk.git
cd ocr-desk
python -m pip install -e .
ocr-desk --version
```

### Usage
English text:
```bash
ocr-desk scan scan.png
```

Arabic + English to a chosen file:
```bash
ocr-desk scan receipt.jpg -l ara+eng -o receipt.txt
```

Create a searchable PDF:
```bash
ocr-desk scan page.tif -l eng -f pdf -o page-searchable.pdf
```

Tune segmentation for a single uniform block and request JSON metadata:
```bash
ocr-desk scan page.png --psm 6 --json
```

List installed languages:
```bash
ocr-desk languages
```

On Windows, if Tesseract is not in `PATH`:
```powershell
ocr-desk --tesseract "C:\Program Files\Tesseract-OCR\tesseract.exe" scan page.png -l ara
```

Use `--overwrite` only when replacing the chosen output is intentional.

### Configuration
OCR Desk has no config file or environment variables. All behavior is explicit CLI input. Defaults are `eng`, `txt`, PSM 3, OEM 3. The selected language must already be installed in Tesseract.

### Project structure
```text
src/ocr_desk/core.py   validation, command construction, safe output workflow
src/ocr_desk/cli.py    command-line interface and exit codes
tests/test_core.py     unit/integration-style wrapper tests
.github/workflows/     cross-platform CI
```

### Testing
The test suite does not require Tesseract because execution is injected and simulated where appropriate:
```bash
python -m unittest discover -s tests -v
```
CI runs installation, tests, and a CLI smoke test on Python 3.10/3.12/3.13 across Ubuntu, Windows, and macOS.

### Preview / screenshots
OCR Desk is intentionally terminal-first, so screenshots are optional. For a project preview, capture `ocr-desk --help`, `ocr-desk languages`, and a successful `scan` command using a non-sensitive sample image. Do not commit private scans merely for screenshots.

### Security & privacy
Recognition happens on the local machine through the selected Tesseract executable. OCR Desk itself performs no network requests. The source image is not modified. OCR output can still contain sensitive information, so protect generated files appropriately. Treat recognized text as untrusted before feeding it into shell commands or other automated systems. See `SECURITY.md`.

### Limitations
- OCR quality depends on Tesseract, the installed language data, image quality, orientation, and layout.
- This release accepts image formats supported by Tesseract; it does not accept PDF as an input document. Convert PDF pages to images first.
- It does not preprocess, deskew, denoise, rotate, or crop images.
- It does not provide a desktop GUI or batch-directory mode yet.
- hOCR is produced by Tesseract with an `.html` output filename.

### Optional roadmap
Possible future additions are batch processing, opt-in image preprocessing, and a lightweight desktop interface. They are not required for the current CLI to work end-to-end.

### Contributing
See `CONTRIBUTING.md`. Keep changes testable, local-first, and documented in both languages.

### License
MIT License — see `LICENSE`.

### Author
**Radwan Abdulhadi Ahmed**  
**رضوان عبدالهادي أحمد**  
GitHub: **@rad03i2**

---

## العربية

### نظرة عامة
OCR Desk أداة سطر أوامر صغيرة وموثوقة تعمل محليًا لتحويل صور المستندات الممسوحة إلى نص أو ملفات قابلة للبحث باستخدام محرك Tesseract OCR. تضيف الأداة واجهة ثابتة، والتحقق من المدخلات، وحماية ملفات الإخراج، ونتائج JSON، واختبارات آلية من دون رفع المستندات إلى خدمة سحابية.

### لماذا المشروع؟
محرك Tesseract قوي، لكن طريقة تحديد صيغ الإخراج وتسميتها قد تكون مربكة داخل السكربتات. يوفر OCR Desk أمرًا واضحًا ومتكرر النتائج للمهام الشائعة مع إبقاء Tesseract هو محرك التعرف الفعلي بصورة صريحة.

### الميزات
- قراءة صور PNG وJPEG وTIFF وBMP وWebP.
- إخراج TXT أو TSV أو hOCR أو PDF قابل للبحث.
- اختيار لغة واحدة أو أكثر مثل `eng` و`ara` و`ara+eng`.
- التحكم في نمط تقسيم الصفحة PSM ونمط المحرك OEM.
- عرض حزم اللغات المثبتة بالأمر `ocr-desk languages`.
- إخراج JSON مناسب للأتمتة.
- تحديد مسار Tesseract يدويًا عند عدم وجوده في PATH.
- منع استبدال الصورة المصدر أو ملف إخراج موجود بصورة عرضية.
- إنشاء ناتج مؤقت أولًا ثم اعتماد الملف المكتمل.
- لا Telemetry ولا حسابات ولا مفاتيح API ولا رفع للمستندات.

### المتطلبات والتثبيت
تحتاج Python 3.10 أو أحدث وTesseract OCR مثبتًا محليًا مع حزم اللغات المطلوبة. لا يتم تضمين Tesseract داخل المشروع عمدًا.

```bash
git clone https://github.com/rad03i2/ocr-desk.git
cd ocr-desk
python -m pip install -e .
ocr-desk --version
```

### أمثلة الاستخدام
استخراج نص عربي وإنجليزي:
```bash
ocr-desk scan document.jpg -l ara+eng -o document.txt
```

إنشاء PDF قابل للبحث:
```bash
ocr-desk scan page.tif -l ara -f pdf -o page-searchable.pdf
```

عرض اللغات المثبتة:
```bash
ocr-desk languages
```

يمكن استخدام `--psm 6` مثلًا لتخطيط كتلة نصية موحدة، و`--json` لإرجاع بيانات النتيجة بصيغة JSON، و`--overwrite` فقط عندما يكون استبدال ملف الإخراج مقصودًا.

### الإعداد
لا يحتاج المشروع ملف إعداد أو متغيرات بيئة. القيم الافتراضية هي اللغة `eng` والصيغة `txt` وPSM 3 وOEM 3. يجب أن تكون اللغة المطلوبة مثبتة أصلًا ضمن Tesseract.

### بنية المشروع
`src/ocr_desk/core.py` يحتوي منطق التحقق والتنفيذ الآمن، و`src/ocr_desk/cli.py` يحتوي واجهة الأوامر، و`tests/test_core.py` يغطي السلوك الأساسي، بينما يحتوي `.github/workflows` إعداد التكامل المستمر متعدد الأنظمة.

### الاختبارات
```bash
python -m unittest discover -s tests -v
```
لا تحتاج الاختبارات إلى Tesseract فعلي لأنها تحاكي عملية التنفيذ عند الحاجة. ويختبر CI الحزمة وواجهة CLI على Ubuntu وWindows وmacOS مع عدة إصدارات Python.

### المعاينة والصور
المشروع موجه للطرفية، لذلك لا يحتاج صور واجهة. عند إضافة صورة تعريفية يفضل إظهار `--help` وقائمة اللغات وأمر OCR ناجح باستخدام صورة تجريبية غير حساسة، وعدم رفع وثائق شخصية لغرض العرض.

### الأمان والخصوصية
المعالجة تتم محليًا عبر ملف Tesseract التنفيذي المختار، ولا ينفذ OCR Desk طلبات شبكة. لا يتم تعديل الصورة الأصلية. قد يحتوي النص الناتج معلومات حساسة، لذلك يجب حماية ملفات الإخراج وعدم تمرير النص المستخرج مباشرة إلى أوامر النظام أو الأتمتة من دون تحقق. راجع `SECURITY.md`.

### القيود
- الدقة تعتمد على Tesseract وحزم اللغة وجودة الصورة واتجاهها وتخطيطها.
- الإصدار الحالي يستقبل الصور المدعومة من Tesseract ولا يستقبل PDF كمدخل؛ يجب تحويل صفحاته إلى صور أولًا.
- لا توجد حاليًا معالجة مسبقة لإزالة التشويش أو تصحيح الميل أو الدوران أو القص.
- لا توجد واجهة رسومية أو معالجة مجلد كامل في الإصدار الحالي.
- ناتج hOCR يُحفظ بامتداد `.html`.

### تطوير اختياري
يمكن مستقبلًا إضافة المعالجة الجماعية، وتحسين الصور اختياريًا، وواجهة سطح مكتب خفيفة. هذه إضافات مستقبلية وليست ميزات مزعومة في الإصدار الحالي.

### المساهمة والترخيص
راجع `CONTRIBUTING.md` للمساهمة. المشروع مرخص بترخيص MIT الموجود في `LICENSE`.

### المؤلف
**Radwan Abdulhadi Ahmed**  
**رضوان عبدالهادي أحمد**  
GitHub: **@rad03i2**
