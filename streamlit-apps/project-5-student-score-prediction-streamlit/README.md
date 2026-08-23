# پروژه ۵: پیش‌بینی نمره‌ی دانش‌آموز

پیش‌بینی نمره‌ی امتحان بر اساس ساعت مطالعه، با استفاده از Linear
Regression. این پروژه علاوه بر مدل، مفهوم Train/Test Split و ارزیابی
دقت مدل با R² Score رو هم پیاده می‌کنه.

## این پروژه چیکار می‌کنه؟
- دیتاست ساعت مطالعه و نمره‌ی دانش‌آموزان رو می‌خونه
- داده رو به بخش آموزش (۸۰٪) و تست (۲۰٪) تقسیم می‌کنه
- مدل رو فقط با داده‌ی آموزش، آموزش می‌ده
- روی داده‌ی تست (که مدل ندیده) ارزیابی می‌کنه و R² Score رو گزارش می‌ده
- نموداری از داده‌ی آموزش، داده‌ی تست، و خط پیش‌بینی رسم می‌کنه

## نحوه‌ی اجرا

pip install numpy pandas matplotlib scikit-learn streamlit

streamlit run student_score_prediction.py


---

# Project 5: Student Score Prediction

Predicts exam scores based on study hours using Linear Regression.
This project also introduces Train/Test Split and model evaluation
using R² Score.

## What this project does
- Reads a dataset of student study hours and exam scores
- Splits the data into 80% training and 20% test sets
- Trains the model using only the training data
- Evaluates it on the unseen test data and reports the R² Score
- Plots the training data, test data, and the regression line

## How to run

pip install numpy pandas matplotlib scikit-learn streamlit

streamlit run student_score_prediction.py
