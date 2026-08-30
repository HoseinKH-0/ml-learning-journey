#============================================================================
# کتابخانه های مورد نیاز: 
# pandas: برای خواندن و پردازش داده‌ها
# matplotlib: برای ترسیم نمودارها و نمایش داده‌ها
# sklearn: برای مدل‌سازی و ارزیابی مدل‌های یادگیری ماشین
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score
from sklearn.preprocessing import StandardScaler
#============================================================================



#============================================================================
# گرفتن یک عدد از کاربر به عنوان مدل یاد گیرنده (1 = LogisticRegression, 2 = DecisionTreeClassifier, 3 = RandomForestClassifier, 4 = KNeighborsClassifier) 
while True:
    try:
        prediction_number = int(input("""
1.LogisticRegression
2.DecisionTreeClassifier
3.RandomForestClassifier
4.KNeighborsClassifier

Enter the desired model number: """))
        
        if prediction_number >= 1 and prediction_number <= 4:
            break
        else:
            print("Invalid number")

    except ValueError:
        print("Invalid input!")
#============================================================================



#============================================================================
# برای جلوگیری از نوشتن کد های تکراری از یک تابع استفاده میکنیم (چون 4 مدل مختلف داریم)
def Error_evaluation(prediction):

    accuracy = accuracy_score(y_test, prediction)
    recall = recall_score(y_test, prediction, pos_label=1)
    precision = precision_score(y_test, prediction, pos_label=1)
    f1 = f1_score(y_test, prediction, pos_label=1)

    return accuracy, recall, precision, f1
#============================================================================



#============================================================================
# خواندن دیتاست heart.csv
data = pd.read_csv("heart.csv")

x = data.drop(["target"], axis=1)
y = data["target"]

# تقسیم کردن داده ها به دو بخش آموزش و تست
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# مقیاس بندی ویژگی ها چون بازه ی اعداد خیلی اختلاف دارن
scaler = StandardScaler()

x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

# آموزش دادن مدل اول با روش لاجستیک رگرسیون
model_1 = LogisticRegression()
model_1.fit(x_train_scaled, y_train)

# آموزش دادن مدل دوم با روش درخت تصمیم
model_2 = DecisionTreeClassifier(max_depth=4, random_state=42)
model_2.fit(x_train_scaled, y_train)

# آموزش دادن مدل سوم با روش جنگل تصادفی
model_3 = RandomForestClassifier(max_depth=4, random_state=42)
model_3.fit(x_train_scaled, y_train)

# آموزش دادن مدل چهارم با روش نزدیک ترین همسایه
model_4 = KNeighborsClassifier(n_neighbors=7)
model_4.fit(x_train_scaled, y_train)
#============================================================================



#============================================================================
# برای هر چهار مدل یک پیشبینی از روی داده های تست میکنیم.
prediction_1 = model_1.predict(x_test_scaled)
prediction_2 = model_2.predict(x_test_scaled)
prediction_3 = model_3.predict(x_test_scaled)
prediction_4 = model_4.predict(x_test_scaled)


predictions = {
    1: prediction_1,
    2: prediction_2,
    3: prediction_3,
    4: prediction_4
}

accuracy, recall, precision, f1 = Error_evaluation(predictions[prediction_number])

print("=---=---=---=---=---=---=---=---=")
print("*** Prediction ***\n")
print(f"Accuracy Score: {accuracy}")
print(f"Recall Score: {recall:.3f}")
print(f"Precision Score: {precision:.3f}")
print(f"F1 Score: {f1:.3f}")
print("=---=---=---=---=---=---=---=---=")
#============================================================================



#============================================================================
# برای نمایش دادن بهتره نتیجه از نمودار میله ای استفاده می کنیم
metrics = ["Accuracy", "Recall", "Precision", "F1"]
scores = [accuracy, recall, precision, f1]

plt.barh(metrics, scores, color=["#10657d", "#0c4959", "#04576e", "#046580"])
plt.xlabel("Score")
plt.title("Model Evaluation Metrics")
plt.show()
#============================================================================
