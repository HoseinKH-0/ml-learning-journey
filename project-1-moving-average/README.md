# پروژه ۱: پیش‌بینی با میانگین متحرک

اولین پروژه‌ی من در مسیر یادگیری ML. یه پیش‌بینی ساده بر پایه‌ی
میانگین چند داده‌ی اخیر، بدون استفاده از هیچ کتابخونه‌ی یادگیری ماشین.

## این پروژه چیکار می‌کنه؟
- یه سری داده‌ی عددی (تصادفی یا وارد شده توسط کاربر) می‌سازه
- با میانگین گرفتن از چند تای آخرین داده، مقدار بعدی رو پیش‌بینی می‌کنه
- خطای هر پیش‌بینی رو نسبت به مقدار واقعی محاسبه و ذخیره می‌کنه
- در پایان، آمار خطاها (میانگین، کمترین، بیشترین) و نموداری از روند خطا نشون می‌ده

## نحوه‌ی اجرا

pip install numpy matplotlib

python moving_average.py


---

# Project 1: Moving Average Prediction

My first project in learning ML. A simple prediction based on the
average of recent data points, without using any ML library.

## What this project does
- Generates a series of numeric data (random or user-entered)
- Predicts the next value using the average of the most recent entries
- Calculates and stores the error of each prediction vs. the actual value
- Shows error statistics (mean, min, max) and a chart of the error trend

## How to run

pip install numpy matplotlib

python moving_average.py
