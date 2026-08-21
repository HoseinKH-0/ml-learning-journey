#============================================================================
#کتابخانه های مورد نیاز:
#pandas: برای خواندن دیتاست
#numpy: برای محاسبات
#matplotlib: برای رسم نمودار
#sklearn: برای آموزش به ماشین و تقسیم بندی داده به دو بخش تست و آموزش
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
#============================================================================


#============================================================================
#خواندن دیتاست مطالعه ی دانش آموز و نمره ی دانش آموز
data = pd.read_csv("student_scores.csv")

#اضافه کردن ستونی به اسم Passed که سطر های آن شامل True و False هستش
data["Passed"] = (data["Scores"] >= 50).astype(int) #astype(int) برای این هستش که مقادیر True و False رو به عدد تبدیل کنیم(True = 1, False = 0)


x = data[["Hours"]]
y = data["Passed"]

#داده هامون رو به دو بخش آموزش (%80) و تست (%20) تقسیم میکنیم
#این کار برای ارزیابی خطا استفاده میشه
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
#============================================================================


#============================================================================
#آموزش دادن به مدل با روش LogisticRegression
model = LogisticRegression()

#اول به مدل داده های آموزشی رو فقط میدیم
model.fit(x_train, y_train)

#پیشبینی مدل روی داده ی تست
prediction = model.predict(x_test)

#محاسبه ی احتمال قبولی برای یه بازه
hours_range = np.linspace(x["Hours"].min(), x["Hours"].max(), 100)

#برای اینکه مدل ورودی دو بعدی می خواد
hours_range_2d = hours_range.reshape(-1, 1)

#فقط ستون دوم رو نگه میداریم
prob_curve = model.predict_proba(hours_range_2d)[:, 1]


#مقایسه میکنیم که ببینم پیشبینی با جواب اصلی چقدر خطا داشتند
#اگه مثلا accuracy برابر با 0.9 بشه یعنی دقت %90 بوده
accuracy = accuracy_score(y_test, prediction)

print(f"Prediction: {prediction}")
print(f"Accuracy: {accuracy:.2f}")
#============================================================================


#============================================================================
#رسم نمودار برای بهتر نشون دادن نتیجه
plt.scatter(x, y, color="blue", label="Actual Data")
plt.plot(hours_range, prob_curve, color="red", label="Predicted Probability")
plt.xlabel("Study Hours")
plt.ylabel("Passed (0 = No, 1 = Yes)")
plt.title("Study Hours vs Pass/Fail")
plt.legend()
plt.show()
#============================================================================
