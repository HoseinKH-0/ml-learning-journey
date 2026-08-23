#============================================================================
#کتابخانه ی numpy برای محاسبات, pandas برای خواندن دیتاست, matplotlib برای رسم نمودار, sklearn برای یاد دادن به مدل و ارزیابی خطا
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import streamlit as st
#============================================================================


#============================================================================
st.title("پروژه ۵: پیش‌بینی نمره‌ی دانش‌آموز")
st.write(""" این پروژه چیکار می‌کنه؟

- دیتاست ساعت مطالعه و نمره‌ی دانش‌آموزان رو می‌خونه
- داده رو به بخش آموزش (۸۰٪) و تست (۲۰٪) تقسیم می‌کنه
- مدل رو فقط با داده‌ی آموزش، آموزش می‌ده
- روی داده‌ی تست (که مدل ندیده) ارزیابی می‌کنه و R² Score رو گزارش می‌ده
- نموداری از داده‌ی آموزش، داده‌ی تست، و خط پیش‌بینی رسم می‌کنه""")
st.caption("این مدل برای نمایش فرآیند ساخت یک اپلیکیشن پیش‌بینی طراحی شده و دقت آن به داده‌های ورودی بستگی دارد.")


#خواندن دیتاست ساعت مطالعه ی دانش آموز و نمره ی دانش آموز
data = pd.read_csv("student_scores.csv")
if st.checkbox("نمایش دیتاست"):
    st.dataframe(data)


x = data[["Hours"]]
y = data["Scores"]

#تقسیم داده 80درصد برای آموزش و 20درصد برای تست، تا بتونیم مدل رو روی داده ای که ندیده امتحان کنیم
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
#============================================================================


#============================================================================
#آموزش دادن به مدل با داده های تمرینی
model = LinearRegression()
model.fit(x_train, y_train)
#============================================================================


#============================================================================
#پیشبینی مدل برای داده های تست(که قبلا ندیده بود)
prediction = model.predict(x_test).round(2)

#نشان دادن دقت مدل(هرچی به یک نزدیک تر باشد یعنی مدل دقیق تر بوده)
r2 = r2_score(y_test, prediction)
#============================================================================


#============================================================================
# نمودار: نقطه‌های آبی = داده‌ی آموزش، نقطه‌های سبز = داده‌ی تست،
# خط قرمز = پیش‌بینی نهایی مدل روی کل بازه‌ی داده
if st.button("نمایش پیشبینی مدل روی داده ی تست"):

    if r2 >= 0.7 or r2 == 1:
        st.success(f"دقت مدل: {r2}")
    elif r2 < 0.7:
        st.warning(f"دقت مدل: {r2}")
    else:
        st.error(f"دقت مدل: {r2}")

    fig, ax = plt.subplots()
    ax.scatter(x_train, y_train, color="blue", label="Training Data")
    ax.scatter(x_test, y_test, color="green", label="Test Data")
    ax.plot(x, model.predict(x), color="red", label="Regression Line")
    ax.set_xlabel("Study Hours")
    ax.set_ylabel("Exam Score")
    ax.set_title("Study Hours vs Exam Score (Train/Test Split)")
    ax.legend()
    st.pyplot(fig)
#============================================================================
