# پروژه ۳: پیش‌بینی دمای ملبورن با scikit-learn

همون مفهوم پروژه‌ی ۲، این‌بار با استفاده از scikit-learn به‌جای
پیاده‌سازی دستی، روی یه دیتاست واقعی و بزرگ.

## این پروژه چیکار می‌کنه؟
- دیتاست دمای کمینه‌ی روزانه‌ی ملبورن (۱۹۸۱ تا ۱۹۹۰) رو با pandas می‌خونه
- یه مدل LinearRegression با scikit-learn می‌سازه و آموزش می‌ده
- دمای روز بعد از آخرین داده رو پیش‌بینی می‌کنه
- نموداری از داده‌های واقعی و خط پیش‌بینی مدل رسم می‌کنه

## نحوه‌ی اجرا

pip install numpy pandas matplotlib scikit-learn

python melbourne_temp_prediction.py



---

# Project 3: Melbourne Temperature Prediction with scikit-learn

Same concept as Project 2, but using scikit-learn instead of a manual
implementation, applied to a real, larger dataset.

## What this project does
- Reads the Melbourne daily minimum temperature dataset (1981-1990) with pandas
- Builds and trains a scikit-learn LinearRegression model
- Predicts the temperature for the day after the last available data point
- Plots the actual data points and the model's regression line

## How to run

pip install numpy pandas matplotlib scikit-learn

python melbourne_temp_prediction.py
