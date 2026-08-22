#============================================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
#============================================================================


#============================================================================
# خوندن دیتاست قیمت خونه‌های تهران
data = pd.read_csv("housePrice.csv")

# حذف Address چون مقدار متنیه و مدل نمی‌تونه مستقیم باهاش کار کنه
# حذف ستون Price(USD) چون می‌خوایم با ستون Price کار کنیم
data = data.drop(["Address", "Price(USD)"], axis=1)

# چند سطر این دیتاست مقدار خراب توی ستون Area داشتن (رشته به‌جای عدد)
# این خط مقادیر نامعتبر رو به NaN تبدیل می‌کنه
data["Area"] = pd.to_numeric(data["Area"], errors="coerce")
data = data.dropna(subset=["Area"])

# x شامل همه‌ی ویژگی‌هایی هست که روی قیمت تأثیر می‌ذارن (همه به جز خود Price)
x = data.drop("Price", axis=1)

# y همون چیزیه که می‌خوایم پیش‌بینی کنیم: قیمت خونه به تومان
y = data["Price"]
#============================================================================


#============================================================================
# ساختن مدل Linear Regression و آموزش دادنش با داده‌های واقعی
model = LinearRegression()
model.fit(x, y)

# پیش‌بینی قیمت یه خونه‌ی فرضی با: متراژ ۶۰، ۲ اتاق، پارکینگ دارد، انباری ندارد، آسانسور دارد
new_house = np.array([[60, 2, 1, 0, 1]])
predicted_price = model.predict(new_house)
print(f"قیمت پیش‌بینی شده برای خونه‌ی جدید: {predicted_price[0]:,.0f} تومان")
#============================================================================


#============================================================================
predicted_all = model.predict(x)

# نمودار: مقایسه‌ی قیمت واقعی با قیمت پیش‌بینی‌شده‌ی مدل، برای همه‌ی خونه‌های دیتاست
plt.scatter(y, predicted_all, s=10, alpha=0.6)
plt.xlabel("Actual Price (Toman)")
plt.ylabel("Predicted Price (Toman)")
plt.title("Actual vs Predicted House Prices in Tehran")
plt.show()
#============================================================================
