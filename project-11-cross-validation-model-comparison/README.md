# پروژه ۱۱: مقایسه‌ی مدل‌ها با Cross-Validation

مقایسه‌ی پنج الگوریتم مختلف Classification (Logistic Regression,
Decision Tree, Random Forest, KNN, SVM) روی دیتاست بیماری قلبی، این‌بار
با استفاده از Cross-Validation به‌جای یک Train/Test Split ثابت.

## این پروژه چیکار می‌کنه؟
- دیتاست heart.csv رو می‌خونه و ویژگی‌ها رو با StandardScaler
  مقیاس‌بندی می‌کنه
- پنج مدل مختلف Classification رو تعریف می‌کنه (بدون آموزش دستی)
- با `cross_val_score` هر مدل رو ۵ بار روی تقسیم‌بندی‌های مختلف داده
  می‌سنجه
- میانگین دقت هر مدل رو در قالب درصد نمایش می‌ده

## نکات یادگیری
- **Cross-Validation**: چرا سنجیدن یک مدل روی چند تقسیم‌بندی مختلف
  (نه فقط یک Train/Test ثابت) تخمین قابل‌اعتمادتری از عملکرد واقعی
  مدل می‌ده، و چطور مشکل «تنظیم دستی پارامتر بر اساس یک تست ثابت»
  (که در پروژه‌های قبلی نگران‌کننده بود) رو کاهش می‌ده
- `cross_val_score` خودش داخلی مدل رو چندین بار از نو آموزش می‌ده؛
  نیازی به `fit` دستی قبل از آن نیست
- **SVM (Support Vector Machine)**: چطور بهترین خط/مرز جداکننده رو
  با بیشترین فاصله از نزدیک‌ترین نمونه‌های هر دسته (Support Vectors)
  پیدا می‌کنه

## نحوه‌ی اجرا
```
pip install pandas scikit-learn
python cross_validation_comparison.py
```

---

# Project 11: Model Comparison with Cross-Validation

Comparing five different Classification algorithms (Logistic
Regression, Decision Tree, Random Forest, KNN, SVM) on the heart
disease dataset, this time using Cross-Validation instead of a single
fixed Train/Test split.

## What this project does
- Reads heart.csv and scales the features with StandardScaler
- Defines five different Classification models (without manually
  training them)
- Uses `cross_val_score` to evaluate each model 5 times on different
  data splits
- Displays each model's average accuracy as a percentage

## What I learned
- **Cross-Validation**: why evaluating a model across multiple splits
  (instead of one fixed Train/Test split) gives a more reliable
  estimate of real performance, and how it reduces the risk of
  "tuning a parameter against one fixed test set" (a concern from
  earlier projects)
- `cross_val_score` internally retrains the model multiple times on
  its own; no manual `fit` is needed beforehand
- **SVM (Support Vector Machine)**: how it finds the best separating
  boundary with the maximum margin from the closest samples of each
  class (Support Vectors)

## How to run
```
pip install pandas scikit-learn
python cross_validation_comparison.py
```
