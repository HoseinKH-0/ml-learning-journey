# 📚 مسیر یادگیری Machine Learning

یک مجموعه پروژه برای یادگیری **ساختاری** Machine Learning - از ساده تا پیچیده.

---

## 🚀 شروع سریع

### نصب کتابخانه‌ها:

```bash
git clone https://github.com/HoseinKH-0/ml-learning-journey
cd ml-learning-journey
pip install -r requirements.txt
```

---

## 📁 پروژه‌ها

### 1️⃣ [**پروژه ۱: میانگین متحرک**](project-1-moving-average/)
- **سطح**: مبتدی
- **موضوع**: پیش‌بینی ساده بدون کتابخانه‌ی ML
- ```bash
  cd project-1-moving-average
  python moving_average.py
  ```

### 2️⃣ [**پروژه ۲: رگرسیون خطی دستی**](project-2-manual-linear-regression/)
- **سطح**: مبتدی
- **موضوع**: پیاده‌سازی فرمول ریاضی Linear Regression
- ```bash
  cd project-2-manual-linear-regression
  python manual_linear_regression.py
  ```

### 3️⃣ [**پروژه ۳: دمای ملبورن با scikit-learn**](project-3-sklearn-linear-regression/)
- **سطح**: میانی
- **موضوع**: استفاده از کتابخانه scikit-learn
- ```bash
  cd project-3-sklearn-linear-regression
  python melbourne_temp_prediction.py
  ```

### 4️⃣ [**پروژه ۴: پیش‌بینی قیمت خانه**](project-4-house-price-prediction/)
- **سطح**: میانی
- **موضوع**: Multiple Linear Regression با چند ویژگی
- ```bash
  cd project-4-house-price-prediction
  python tehran_house_price.py
  ```

### 5️⃣ [**پروژه ۵: نمره‌ی دانش‌آموز**](project-5-student-score-prediction/)
- **سطح**: میانی
- **موضوع**: Train/Test Split و ارزیابی مدل
- ```bash
  cd project-5-student-score-prediction
  python student_score_prediction.py
  ```

### 6️⃣ [**پروژه ۶: قبولی دانش‌آموز (Classification)**](project-6-student-pass-fail-prediction/)
- **سطح**: پیشرفته
- **موضوع**: Classification و Logistic Regression
- ```bash
  cd project-6-student-pass-fail-prediction
  python student_pass_fail_prediction.py
  ```

### 7️⃣ [**پروژه ۷: بقاء کشتی تایتانیک (Classification)**](project-7-titanic-classification/)
- **سطح**: پیشرفته
- **موضوع**: Classification با Logistic Regression
- ```bash
  cd project-7-titanic-classification
  python titanic_classification.py
  ```

### 8️⃣ [**پروژه ۸: بقاء تایتانیک با Decision Tree**](project-8-titanic-decision-tree/)
- **سطح**: پیشرفته
- **موضوع**: Decision Tree و Hyperparameter Tuning (max_depth)
- ```bash
  cd project-8-titanic-decision-tree
  python titanic_decision_tree.py
  ```

### 9️⃣ [**پروژه ۹: بقاء تایتانیک با Random Forest**](project-9-titanic-random-forest/)
- **سطح**: پیشرفته
- **موضوع**: Random Forest (Ensemble Learning) و رسم درخت‌های داخلی
- ```bash
  cd project-9-titanic-random-forest
  python titanic_random_forest.py
  ```

### 🔟 [**پروژه ۱۰: تشخیص بیماری قلبی (مقایسه‌ی چند مدل)**](project-10-heart-disease-classification/)
- **سطح**: پیشرفته
- **موضوع**: مقایسه‌ی Logistic Regression, Decision Tree, Random Forest
  با معیارهای Accuracy, Recall, Precision, F1-Score
- ```bash
  cd project-10-heart-disease-classification
  python heart_disease_classification.py
  ```

---

## 🖥️ اپ‌های تعاملی (Streamlit)

نسخه‌ی تعاملی و کاربرپسند چند تا از پروژه‌های بالا، ساخته‌شده با
Streamlit - برای تمرین ساخت رابط کاربری روی مدل‌های ML.

📁 پوشه: [`streamlit-apps/`](streamlit-apps/)

### نحوه‌ی اجرا:
```bash
cd Streamlit-apps
cd <foldername>
streamlit run <filename>.py
```

---

## 📦 نیازمندی‌ها

- Python 3.8+
- NumPy، Pandas، Matplotlib، Scikit-learn، Streamlit

(همه در `requirements.txt`)
