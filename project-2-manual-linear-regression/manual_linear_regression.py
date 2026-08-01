#=======================================================================================
import numpy as np
import matplotlib.pyplot as plt
#=======================================================================================



#=======================================================================================
while True:
    try:
        today_tem = int(input("لطفا دمای امروز را وارد کنید: "))
        if today_tem >= -30 and today_tem <= 55:
            break
        else:
            print("لطفا دمایی بین -30 تا 55 وارد کنید.")
    
    except ValueError:
        print("لطفا یک عدد صحیح وارد کنید.")
#=======================================================================================



#=======================================================================================
with open("temperatures.txt", "a") as file:
    file.write(f"{today_tem}\n")
with open("temperatures.txt", "r") as file:
    content = file.read()
lines = content.splitlines()
new_lines = []

for i in lines:
    new_lines.append(int(i))


x = []
y = new_lines
for i in range(len(new_lines)):
    x.append(i + 1)
#=======================================================================================



#=======================================================================================
x = np.array(x)
y = np.array(y)


avg_x = np.mean(x)
avg_y = np.mean(y)

new_x = x - avg_x
new_y = y - avg_y


numerator = sum(new_x * new_y)
denominator = sum(new_x ** 2)


m = (numerator / denominator).round(2)
b = (avg_y - (m * avg_x)).round(2)
#=======================================================================================



#=======================================================================================
day_to_predict = len(new_lines) + 1
prediction = (m * day_to_predict + b).round(2)
print(f"پیشبینی برای روز {day_to_predict} برابر است با: {prediction}")
#=======================================================================================



#=======================================================================================
plt.scatter(x, y, label="Actual Temperature")
plt.plot(x, m * x + b, color="red", label="Regression Line")
plt.xlabel("Day Number")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Prediction using Linear Regression")
plt.legend()
plt.show()
#=======================================================================================
