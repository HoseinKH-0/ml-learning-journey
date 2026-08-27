# پروژه ۷: پیش‌بینی بقاء در کشتی تایتانیک (دسته‌بندی)

پیش‌بینی بقاء مسافران کشتی تایتانیک بر اساس ویژگی‌های مختلف (جنسیت، سن، کلاس سفر و...)
با استفاده از الگوریتم‌های Classification مختلف. این پروژه یکی از معروف‌ترین دیتاست‌های
دنیای Data Science و Machine Learning است.

## این پروژه چیکار می‌کنه؟
- دیتاست تایتانیک (۸۹۱ مسافر) رو از یه فایل CSV می‌خونه
- داده‌ها رو تمیز می‌کنه (حذف مقادیر خالی، تبدیل متغیرهای رشته‌ای به عددی)
- ویژگی‌های مرتبط (سن، جنسیت، کلاس سفر، قیمت بلیط) را انتخاب می‌کنه
- داده رو به بخش آموزش (۸۰٪) و تست (۲۰٪) تقسیم می‌کنه
- Confusion Matrix و نموداری از دقت مدل‌ها رسم می‌کنه

## نحوه‌ی اجرا

```bash
pip install numpy pandas matplotlib scikit-learn streamlit
```

```bash
streamlit run titanic_classification.py
```

---

# Project 7: Titanic Survival Prediction (Classification)

Predicting the survival of Titanic passengers based on various features
(gender, age, ticket class, etc.) using different Classification algorithms.
This is one of the most famous datasets in the Data Science and Machine Learning world.

## What this project does
- Reads the Titanic dataset (891 passengers) from a CSV file
- Cleans the data (handles missing values, converts categorical variables to numeric)
- Selects relevant features (age, gender, passenger class, ticket price)
- Splits the data into 80% training and 20% test sets
- Builds and trains multiple Classification models (Logistic Regression, Decision Tree, Random Forest)
- Evaluates each model and reports accuracy using Accuracy, Precision, Recall, and F1-Score
- Plots the Confusion Matrix and a comparison chart of model accuracies

## How to run

```bash
pip install numpy pandas matplotlib scikit-learn streamlit
```

```bash
streamlit run titanic_classification.py
```
