#============================================================================
# کتابخونه‌های لازم برای کار با آرایه، خوندن فایل CSV، رسم نمودار، و ساختن مدل رگرسیون خطی
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression 
#============================================================================



#============================================================================
# خوندن دیتاست دمای کمینه‌ی روزانه‌ی ملبورن (از سال 1981 تا 1990)
data = pd.read_csv("daily-min-temperatures.csv")
temp = data["Temp"].values
x = []
y = temp
for i in range(len(temp)):
    x.append(i + 1)
x = np.array(x).reshape(-1, 1)
#============================================================================



#============================================================================
# ساختن مدل Linear Regression و آموزش دادنش با داده‌های واقعی 
model = LinearRegression()
model.fit(x, y)
#============================================================================



#============================================================================
# نمایش پیشبینی دما برای یک روز جلو تراز اخرین داده ای که داریم
day_to_predict = np.array([[len(temp) + 1]])
prediction = model.predict(day_to_predict)
print(f"دمای پیشبینی شده: {prediction[0]:.2f}")
#============================================================================



#============================================================================
# نمودار: نقطه‌های دمای واقعی (آبی) + خط پیش‌بینی مدل (قرمز)
plt.scatter(x, y, label="Actual Temperature", s=5, alpha=0.5)
plt.plot(x, model.predict(x), color="red", label="Regression Line", linewidth=2)
plt.xlabel("Day Number")
plt.ylabel("Temperature (°C)")
plt.title("Melbourne Daily Minimum Temperature Prediction")
plt.legend()
plt.show()
#============================================================================
