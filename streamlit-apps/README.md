# اپلیکیشن های Streamlit

- - -

این مجموعه شامل ۵ پروژه‌ی اصلی گیت‌هابم هستش که با Streamlit ساخته شده.
هدف از ساخت این اپلیکیشن‌ها، نمایش قابلیت‌های مدل‌ها در یک محیط زیبا و کاربرپسند است.

- - -

## 📁 اپلیکیشن‌های موجود

1. **melbourne_temp_prediction.py** - پیش‌بینی دمای ملبورن (Linear Regression)
2. **tehran_house_price.py** - پیش‌بینی قیمت خونه‌ی تهران (Multiple Regression)
3. **student_score_prediction.py** - پیش‌بینی نمره‌ی دانش‌آموز (Train/Test Split)
4. **student_pass_fail_prediction.py** - پیش‌بینی قبولی دانش‌آموز (Logistic Regression)
5. **titanic_classification.py** - پیش‌بینی بقاء تایتانیک (Classification)

- - -

## نحوه‌ی نصب و اجرا

1. ابتدا کتابخانه‌ها را نصب کنید:
```bash
pip install -r requirements.txt
```
2. به این پوشه بروید:
```bash
cd Streamlit-apps
```
3. هر پروژه را با دستور زیر اجرا کنید:
```bash
streamlit run [اسم پروژه].py
```
4. مرورگر شما به طور خودکار باز می‌شود و برنامه را نمایش می‌دهد.

- - -

## عیب‌یابی

اگر با خطای **ModuleNotFoundError: No Module Named '...'** روبه‌رو شدید:

1. می‌توانید کتابخانه‌ها را دستی نصب کنید:
```bash
pip install [اسم کتابخانه]
```
2. اگر باز هم با ارور مواجه شدید، بهترین راه استفاده از محیط مجازی هست. با زدن دستورات زیر در ترمینال می‌توانید محیط مجازی بسازید:
```bash
python -m venv .venv
```
```bash
.venv/Scripts/Activate
```
حالا که محیط مجازی فعال است، می‌توانید داخل آن کتابخانه‌ها را نصب کنید:
```bash
pip install [اسم کتابخانه]
```

- - -
