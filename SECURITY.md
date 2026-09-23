# Security Policy

## Scope

OCR Desk is designed for local document processing. It invokes the Tesseract executable selected by the user or discovered on the system path. The project itself does not upload document images or recognized text to a remote OCR service.

## Safe use

- Install Tesseract from a trusted source.
- Treat recognized text as untrusted input before passing it to shells, templates, databases, or automation systems.
- OCR Desk refuses to replace an existing output unless overwrite behavior is explicitly requested.
- The source image is not intentionally modified.
- Protect generated output when it contains personal, confidential, or sensitive information.

## Reporting a security issue

For non-sensitive problems, open a GitHub issue with a minimal reproduction that contains no confidential documents or credentials.

For sensitive security reports, do not publish private data in a public issue. Use GitHub private vulnerability reporting if it is available for this repository.

---

<div dir="rtl" align="right">

# سياسة الأمان

## نطاق المشروع

صُمم OCR Desk لمعالجة المستندات محليًا على جهاز المستخدم. يستدعي البرنامج محرك التعرّف المثبّت على الجهاز، ولا يرفع المشروع نفسه صور المستندات أو النصوص المستخرجة إلى خدمة تعرّف خارجية.

## الاستخدام الآمن

- ثبّت محرك التعرّف من مصدر موثوق.
- تعامل مع النص المستخرج على أنه مدخل غير موثوق قبل تمريره إلى أوامر النظام أو قواعد البيانات أو قوالب البرامج أو عمليات الأتمتة.
- لا يستبدل المشروع ملف إخراج موجودًا إلا عند طلب ذلك صراحة.
- لا يتم تعديل الصورة الأصلية بصورة مقصودة.
- احمِ ملفات النتائج إذا كانت تحتوي معلومات شخصية أو سرية أو حساسة.

## الإبلاغ عن مشكلة أمنية

للمشكلات غير الحساسة يمكن فتح مشكلة على GitHub مع مثال مبسط لا يحتوي على مستندات خاصة أو بيانات دخول.

أما البلاغات الأمنية الحساسة فلا تنشر معلوماتها في مشكلة عامة. استخدم الإبلاغ الخاص عن الثغرات في GitHub إذا كان مفعّلًا للمستودع.

## المشرف

**رضوان عبدالهادي أحمد**  
**Radwan Abdulhadi Ahmed**  
GitHub: **@rad03i2**

</div>
