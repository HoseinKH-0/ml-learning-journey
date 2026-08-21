# پروژه ۶: پیش‌بینی قبولی دانش‌آموز (دسته‌بندی)

اولین پروژه‌ی من با Classification (دسته‌بندی) به‌جای Regression. با
استفاده از Logistic Regression، بر اساس ساعت مطالعه پیش‌بینی می‌کنم
دانش‌آموز قبول می‌شه یا نه (نه اینکه نمره‌ش دقیقاً چقدر می‌شه).

## این پروژه چیکار می‌کنه؟
- از همون دیتاست ساعت مطالعه/نمره استفاده می‌کنه، ولی یه ستون جدید
  می‌سازه: قبول (نمره ≥ ۵۰) یا رد (نمره < ۵۰)
- داده رو به بخش آموزش و تست تقسیم می‌کنه
- یه مدل Logistic Regression می‌سازه و آموزش می‌ده
- دقت مدل رو با Accuracy Score ارزیابی می‌کنه
- منحنی احتمال قبولی (Sigmoid Curve) رو در کنار داده‌های واقعی رسم می‌کنه

## نحوه‌ی اجرا
```bash
pip install pandas numpy matplotlib scikit-learn
```
```bash
python student_pass_fail_prediction.py
```

---

# Project 6: Student Pass/Fail Prediction (Classification)

My first Classification project instead of Regression. Using Logistic
Regression, I predict whether a student passes or fails based on
study hours (not their exact score).

## What this project does
- Uses the same study hours/scores dataset, but adds a new column:
  Passed (score ≥ 50) or Failed (score < 50)
- Splits the data into training and test sets
- Builds and trains a Logistic Regression model
- Evaluates accuracy using Accuracy Score
- Plots the predicted probability curve (Sigmoid Curve) alongside actual data points

## How to run
```bash
pip install pandas numpy matplotlib scikit-learn
```
```bash
python student_pass_fail_prediction.py
```
