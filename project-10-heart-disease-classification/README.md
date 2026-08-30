# پروژه ۱۰: تشخیص بیماری قلبی (مقایسه‌ی چند مدل)

پیش‌بینی وجود بیماری قلبی در بیماران با استفاده از چهار الگوریتم مختلف
Classification (Logistic Regression, Decision Tree, Random Forest,
KNN)، با امکان انتخاب مدل توسط کاربر و نمایش معیارهای ارزیابی کامل.

## این پروژه چیکار می‌کنه؟
- دیتاست واقعی بیماری قلبی (UCI Heart Disease Dataset) رو می‌خونه
- داده رو به بخش آموزش و تست تقسیم می‌کنه، و ویژگی‌ها رو با
  StandardScaler مقیاس‌بندی می‌کنه
- چهار مدل مختلف Classification رو می‌سازه و آموزش می‌ده
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
- `max_depth` عمق درخت رو محدود می‌کنه، هم برای Decision Tree هم
  برای هر درخت داخل Random Forest
- **Feature Scaling**: چرا اختلاف مقیاس بین ویژگی‌ها (مثل کلسترول در
  مقابل oldpeak) باعث کندی یا عدم همگرایی Logistic Regression میشه،
  و چطور StandardScaler این مشکل رو حل می‌کنه
- فرق `fit_transform` (روی train) و `transform` (روی test) و چرا این
  ترتیب برای جلوگیری از Data Leakage حیاتیه
- **KNN (K-Nearest Neighbors)**: چطور بر پایه‌ی فاصله با نزدیک‌ترین
  نمونه‌های آموزشی و رأی اکثریت، پیش‌بینی می‌کنه؛ و چرا این الگوریتم
  حتماً به Feature Scaling نیاز داره
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

Predicting the presence of heart disease using four different
Classification algorithms (Logistic Regression, Decision Tree, Random
Forest, KNN), with user-selectable model and full evaluation metrics.

## What this project does
- Reads the real UCI Heart Disease dataset
- Splits the data into training and test sets, and scales features
  using StandardScaler
- Builds and trains four different Classification models
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
- `max_depth` limits tree depth, both for a single Decision Tree and
  for every tree inside a Random Forest
- **Feature Scaling**: why differing feature scales (e.g. cholesterol
  vs. oldpeak) cause Logistic Regression to converge slowly or not at
  all, and how StandardScaler fixes this
- The difference between `fit_transform` (on train) and `transform`
  (on test), and why this order matters to avoid data leakage
- **KNN (K-Nearest Neighbors)**: how it predicts based on distance to
  the nearest training samples and majority vote, and why it strictly
  requires feature scaling
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
