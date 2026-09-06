#============================================================================
# ماژول های مورد نیاز:
# pandas: برای خواندن دیتاست
# sklearn: برای آموزش دادن مدل های مختلف و ارزیابی خطا
import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
#============================================================================


#============================================================================
# خواندن دیتاست heart.csv
data = pd.read_csv("heart.csv")

x = data.drop(["target"], axis=1)
y = data["target"]

# مقیاس‌بندی ویژگی‌ها (میانگین=0، انحراف معیار=1) چون بعضی مدل‌ها (مثل Logistic Regression و SVC)
# به اختلاف بازه‌ی اعداد بین ویژگی‌ها حساسن
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

models = {
    "LogisticRegression": LogisticRegression(),
    "DecisionTreeClassifier": DecisionTreeClassifier(max_depth=4, random_state=42),
    "RandomForestClassifier": RandomForestClassifier(max_depth=4, random_state=42),
    "KNeighborsClassifier": KNeighborsClassifier(n_neighbors=7),
    "SVC": SVC()
}
#============================================================================


#============================================================================
# cross_val_score: برای ارزیابی خطا برای هر مدل
for name, model in models.items():
    scores = cross_val_score(model, x_scaled, y, cv=5) # cv=5: یعنی برای هر مدل داده ها رو 5 بار به صورت مختلف به دو دسته آموزش و تست تقسیم کن
    print(f"{name} - Average Accuracy: {scores.mean() * 100:.2f}%") # نمایش میانگین هر مدل
#============================================================================