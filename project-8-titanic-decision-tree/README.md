# پروژه ۸: پیش‌بینی بقای تایتانیک با Decision Tree

مقایسه‌ی Decision Tree با Logistic Regression (پروژه‌ی ۷) روی همون
دیتاست تایتانیک، برای دیدن تفاوت عملکرد دو الگوریتم مختلف روی یه
مسئله‌ی یکسان.

## این پروژه چیکار می‌کنه؟
- از همون داده‌ی پاک‌سازی‌شده‌ی پروژه‌ی ۷ استفاده می‌کنه
- یه مدل DecisionTreeClassifier می‌سازه و آموزش می‌ده
- با تنظیم `max_depth` (Hyperparameter Tuning)، از Overfitting جلوگیری می‌کنه
- نتیجه رو با Accuracy و Confusion Matrix ارزیابی می‌کنه

## نکات یادگیری
- Decision Tree می‌تونه هم برای Classification و هم Regression استفاده بشه
- محدود کردن عمق درخت (`max_depth`) جلوی بیش‌برازش (Overfitting) رو می‌گیره
- هیچ مدلی همیشه از بقیه بهتر نیست؛ باید چند مدل رو مقایسه کرد

## نحوه‌ی اجرا
```bash
pip install pandas numpy matplotlib scikit-learn
```
```bash
python titanic_decision_tree.py
```

---

# Project 8: Titanic Survival Prediction with Decision Tree

Comparing Decision Tree with Logistic Regression (Project 7) on the
same Titanic dataset, to see how different algorithms perform on the
same problem.

## What this project does
- Uses the same cleaned data from Project 7
- Builds and trains a DecisionTreeClassifier
- Tunes `max_depth` (Hyperparameter Tuning) to prevent overfitting
- Evaluates results with Accuracy and Confusion Matrix

## What I learned
- Decision Trees can be used for both Classification and Regression
- Limiting tree depth (`max_depth`) helps prevent overfitting
- No single model is always best; comparing models matters

## How to run
```bash
pip install pandas numpy matplotlib scikit-learn
```
```bash
python titanic_decision_tree.py
```