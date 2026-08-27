#============================================================================
# کتابخانه های مورد نیاز: 
# numpy: برای انجام محاسبات عددی و کار با آرایه‌ها
# pandas: برای خواندن و پردازش داده‌ها
# matplotlib: برای ترسیم نمودارها و نمایش داده‌ها
# sklearn: برای مدل‌سازی و ارزیابی مدل‌های یادگیری ماشین
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.tree import plot_tree
#============================================================================


#============================================================================
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
#============================================================================

#============================================================================
# تقسیم داده‌ها به ویژگی‌ها (X) و برچسب‌ها (y)
x = data.drop("Survived", axis=1)
y = data["Survived"]

# تقسیم داده ها به دو بخش آموزشی (80%) و تستی (20%)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
#============================================================================

#============================================================================
# آموزش دادن مدل با استفاده از روش RandomForestClassifier
model = RandomForestClassifier()
model.fit(x_train, y_train)

# پیشبینی روی داده ی تست
prediction = model.predict(x_test)

# محاسبه ی دقت مدل
accuracy = accuracy_score(y_test, prediction)
cm = confusion_matrix(y_test, prediction)


one_tree = model.estimators_[0]


print("Accuracy:", accuracy)
print("Confusion Matrix:\n", cm)
#============================================================================

#============================================================================
# رسم نمودار برای اولین درخت
plt.figure(figsize=(20, 10))
plot_tree(one_tree, feature_names=x.columns, class_names=["Died", "Survived"], filled=True, max_depth=3)
plt.show()
#============================================================================