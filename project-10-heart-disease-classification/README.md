# پروژه ۱۰: تشخیص بیماری قلبی (مقایسه‌ی چند مدل)

پیش‌بینی وجود بیماری قلبی در بیماران با استفاده از سه الگوریتم مختلف
Classification (Logistic Regression, Decision Tree, Random Forest)،
با امکان انتخاب مدل توسط کاربر و نمایش معیارهای ارزیابی کامل.

## این پروژه چیکار می‌کنه؟
- دیتاست واقعی بیماری قلبی (UCI Heart Disease Dataset) رو می‌خونه
- سه مدل مختلف Classification رو می‌سازه و آموزش می‌ده
- از کاربر می‌پرسه کدوم مدل رو می‌خواد ببینه (با مدیریت خطای ورودی)
- نتیجه‌ی مدل انتخاب‌شده رو با ۴ معیار ارزیابی می‌کنه: Accuracy,
  Recall, Precision, F1-Score
- یه نمودار میله‌ای افقی از این ۴ معیار رسم می‌کنه

## نکات یادگیری
- Precision و Recall چه فرقی با هم دارن و چرا Recall توی مسائل
  پزشکی معمولاً اهمیت بیشتری داره (از دست ندادن بیماران واقعی)
- `pos_label` برای مشخص کردن صریح اینکه کدوم کلاس «مثبت» حساب می‌شه
- `random_state` فقط برای تکرارپذیری نتایجه، نه برای پیدا کردن
  «بهترین» نتیجه با امتحان کردن مقادیر مختلف
- `max_depth` عمق درخت رو محدود می‌کنه (طولانی‌ترین مسیر از ریشه تا
  برگ)، هم برای Decision Tree هم برای هر درخت داخل Random Forest
- استفاده از تابعی که چند مقدار را با `return` برمی‌گردونه
- استفاده از دیکشنری برای انتخاب پویا بین چند متغیر بر اساس ورودی کاربر

## نحوه‌ی اجرا
```
pip install pandas numpy matplotlib scikit-learn
python heart_disease_classification.py
```

⚠️ توجه: این دیتاست قدیمی و کوچیکه (۳۰۳ نمونه) و صرفاً برای یادگیری
تکنیک Classification استفاده شده، نه برای تشخیص واقعی پزشکی.

---

# Project 10: Heart Disease Classification (Model Comparison)

Predicting the presence of heart disease using three different
Classification algorithms (Logistic Regression, Decision Tree, Random
Forest), with user-selectable model and full evaluation metrics.

## What this project does
- Reads the real UCI Heart Disease dataset
- Builds and trains three different Classification models
- Asks the user which model to view (with input validation)
- Evaluates the chosen model's predictions with 4 metrics: Accuracy,
  Recall, Precision, F1-Score
- Plots a horizontal bar chart of these 4 metrics

## What I learned
- The difference between Precision and Recall, and why Recall usually
  matters more in medical problems (not missing real patients)
- Using `pos_label` to explicitly state which class counts as "positive"
- `random_state` is only for reproducibility, not for hunting the
  "best" result by trying different values
- `max_depth` limits tree depth (the longest root-to-leaf path), both
  for a single Decision Tree and for every tree inside a Random Forest
- Using a function that returns multiple values with `return`
- Using a dictionary to dynamically select between variables based on
  user input

## How to run
```
pip install pandas numpy matplotlib scikit-learn
python heart_disease_classification.py
```


⚠️ Note: this dataset is old and small (303 samples) and was used
purely to learn Classification techniques, not for real medical diagnosis.
