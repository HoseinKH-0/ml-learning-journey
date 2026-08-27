# پروژه ۹: پیش‌بینی بقاء تایتانیک با Random Forest

مقایسه‌ی Random Forest با Decision Tree (پروژه‌ی ۸) و Logistic Regression
(پروژه‌ی ۷) روی همون دیتاست تایتانیک، برای دیدن تفاوت عملکرد یه مدل
ترکیبی (Ensemble) نسبت به مدل‌های تکی.

## این پروژه چیکار می‌کنه؟
- از همون داده‌ی پاک‌سازی‌شده‌ی پروژه‌های قبلی استفاده می‌کنه
- یه مدل RandomForestClassifier می‌سازه و آموزش می‌ده (ترکیبی از صدها
  Decision Tree)
- نتیجه رو با Accuracy و Confusion Matrix ارزیابی می‌کنه
- یکی از درخت‌های داخل جنگل رو با `plot_tree` رسم می‌کنه تا ساختار
  سوال‌پرسیدن مدل قابل‌مشاهده باشه

## نکات یادگیری
- Random Forest از ترکیب رأی چند Decision Tree (که هرکدوم روی
  زیرمجموعه‌ی متفاوتی از داده آموزش دیدن) تصمیم نهایی می‌گیره
- این ترکیب معمولاً از یه Decision Tree تنها دقیق‌تر و پایدارتره
  (کمتر دچار Overfitting می‌شه)


## نحوه‌ی اجرا
```
pip install pandas numpy matplotlib scikit-learn
python titanic_random_forest.py
```

---

# Project 9: Titanic Survival Prediction with Random Forest

Comparing Random Forest with Decision Tree (Project 8) and Logistic
Regression (Project 7) on the same Titanic dataset, to see how an
ensemble model performs compared to single models.

## What this project does
- Uses the same cleaned data from previous projects
- Builds and trains a RandomForestClassifier (an ensemble of hundreds
  of Decision Trees)
- Evaluates results with Accuracy and Confusion Matrix
- Plots one tree from inside the forest with `plot_tree` to visualize
  how the model asks questions

## What I learned
- Random Forest combines the votes of many Decision Trees (each trained
  on a different subset of data) to make a final decision
- This combination is usually more accurate and stable than a single
  Decision Tree (less prone to overfitting)


## How to run
```
pip install pandas numpy matplotlib scikit-learn
python titanic_random_forest.py
```
