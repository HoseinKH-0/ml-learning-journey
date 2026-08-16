#============================================================================
#کتابخانه ی numpy برای محاسبات, pandas برای خواندن دیتاست, matplotlib برای رسم نمودار, sklearn برای یاد دادن به مدل و ارزیابی خطا
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
#============================================================================


#============================================================================
#خواندن دیتاست ساعت مطالعه ی دانش آموز و نمره ی دانش آموز
data = pd.read_csv("student_scores.csv")

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
print(prediction)

#نشان دادن دقت مدل(هرچی به یک نزدیک تر باشد یعنی مدل دقیق تر بوده)
r2 = r2_score(y_test, prediction)
print(f"R2 score: {r2}")
#============================================================================


#============================================================================
# نمودار: نقطه‌های آبی = داده‌ی آموزش، نقطه‌های سبز = داده‌ی تست،
# خط قرمز = پیش‌بینی نهایی مدل روی کل بازه‌ی داده
plt.scatter(x_train, y_train, color="blue", label="Training Data")
plt.scatter(x_test, y_test, color="green", label="Test Data")
plt.plot(x, model.predict(x), color="red", label="Regression Line")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.title("Study Hours vs Exam Score (Train/Test Split)")
plt.legend()
plt.show()
#============================================================================
