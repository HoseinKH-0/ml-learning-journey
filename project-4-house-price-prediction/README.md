# پروژه ۴: پیش‌بینی قیمت خانه با رگرسیون چندمتغیره

پیش‌بینی قیمت خونه‌های تهران با استفاده از چند ویژگی همزمان
(Multiple Linear Regression)، روی یه دیتاست واقعی و نسبتاً کثیف.

## این پروژه چیکار می‌کنه؟
- دیتاست قیمت خونه‌های تهران رو از یه فایل CSV می‌خونه
- داده‌ها رو پاک‌سازی می‌کنه (حذف ستون‌های غیرضروری، تبدیل مقادیر
  نامعتبر، حذف سطرهای خراب)
- با ویژگی‌های متراژ، تعداد اتاق، پارکینگ، انباری و آسانسور، یه مدل
  رگرسیون چندمتغیره می‌سازه
- برای یه خونه‌ی فرضی، قیمت رو پیش‌بینی می‌کنه
- نموداری از مقایسه‌ی قیمت واقعی با قیمت پیش‌بینی‌شده رسم می‌کنه

## نحوه‌ی اجرا

pip install numpy pandas matplotlib scikit-learn
python tehran_house_price.py



⚠️ توجه: قیمت‌های این دیتاست مربوط به سال‌های قدیم‌تره و با بازار
امروز هم‌خونی نداره. هدف این پروژه صرفاً یادگیری تکنیک بود.

---

# Project 4: House Price Prediction with Multiple Regression

Predicting Tehran house prices using several features at once
(Multiple Linear Regression), on a real and fairly messy dataset.

## What this project does
- Reads the Tehran house price dataset from a CSV file
- Cleans the data (drops unnecessary columns, converts invalid values,
  removes corrupted rows)
- Builds a multiple regression model using area, room count, parking,
  warehouse, and elevator as features
- Predicts the price for a hypothetical house
- Plots actual vs. predicted prices

## How to run

pip install numpy pandas matplotlib scikit-learn
python tehran_house_price.py


⚠️ Note: prices in this dataset reflect an older time period and do
not match current market prices. This project was purely for learning purposes.
