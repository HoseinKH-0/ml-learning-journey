#============================================================================
# کتابخانه های مورد نیاز: 
# numpy: برای انجام محاسبات عددی و کار با آرایه‌ها
# pandas: برای خواندن و پردازش داده‌ها
# matplotlib: برای ترسیم نمودارها و نمایش داده‌ها
# sklearn: برای مدل‌سازی و ارزیابی مدل‌های یادگیری ماشین
# streamlit: برای نمایش دادن بهتر برنامه
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
import streamlit as st
#============================================================================


#============================================================================
st.title("پروژه ۷: پیش‌بینی بقاء در کشتی تایتانیک (دسته‌بندی)")
st.write("""این پروژه چیکار می‌کنه؟

دیتاست تایتانیک (۸۹۱ مسافر) رو از یه فایل می‌خونه
داده‌ها رو تمیز می‌کنه (حذف مقادیر خالی، تبدیل متغیرهای رشته‌ای به عددی)
ویژگی‌های مرتبط (سن، جنسیت، کلاس سفر، قیمت بلیط) را انتخاب می‌کنه
داده رو به بخش آموزش (۸۰٪) و تست (۲۰٪) تقسیم می‌کنه
هر مدل رو ارزیابی می‌کنه و دقت هر یک رو با Accuracy و گزارش می‌ده
Confusion Matrix و نموداری از دقت مدل‌ها رسم می‌کنه""")
st.caption("این مدل برای نمایش فرآیند ساخت یک اپلیکیشن پیش‌بینی طراحی شده و دقت آن به داده‌های ورودی بستگی دارد.")

# خواندن داده های دیتاست Titanic
data = pd.read_csv('titanic.csv')

# حذف ستون های غیر ضروری از دیتاست
data = data.drop(["PassengerId", "Name", "Ticket", "Cabin"], axis=1)

# پر کردن مقادیر خالی در ستون Age با استفاده از میانگین
data["Age"] = data["Age"].fillna(data["Age"].mean())

# پر کردن مقادیر خالی ستون Embarked با استفاده از مد
data["Embarked"] = data["Embarked"].fillna(data["Embarked"].mode()[0])

# تبدیل مقادیر متنی ستون Sex به 0 و 1 (0 برای مرد و 1 برای زن)
data["Sex"] = data["Sex"].map({"male": 0, "female": 1})

# تغییر مقادیر متنی ستون Embarked به مقادیر عددی با استفاده از one-hot encoding
data = pd.get_dummies(data, columns=["Embarked"], dtype=int)

if st.checkbox("نمایش دیتاست"):
    st.dataframe(data)
#============================================================================

#============================================================================
# تقسیم داده‌ها به ویژگی‌ها (X) و برچسب‌ها (y)
x = data.drop("Survived", axis=1)
y = data["Survived"]

# تقسیم داده ها به دو بخش آموزشی (80%) و تستی (20%)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
#============================================================================



#============================================================================
# آموزش مدل با استفاده از روش LogisticRegression
model = LogisticRegression()

# آموزش دادن به مدل با داده های آموزشی
model.fit(x_train, y_train)

# پیش‌بینی نتایج با استفاده از داده‌های تست
prediction = model.predict(x_test)

# محاسبه ی دقت مدل
accuracy = accuracy_score(y_test, prediction)
cm = confusion_matrix(y_test, prediction)

if st.button("نمایش پیشبینی مدل روی داده تست"):
    st.success(f"پیشبینی داده ی تست: {prediction}")
    st.success(f"دقت مدل: {accuracy}")
    st.success(f"ConfusionMatrix: {cm}")

    # نمایش ماتریس سردرگمی با استفاده از ConfusionMatrixDisplay
    fig, ax = plt.subplots()
    disp = ConfusionMatrixDisplay.from_predictions(y_test, prediction, display_labels=["Died", "Survived"])
    disp.plot(ax=ax, cmap='Blues', values_format='d')
    ax.set_title("Confusion Matrix - Titanic Survival Prediction")
    st.pyplot(fig)
#============================================================================
