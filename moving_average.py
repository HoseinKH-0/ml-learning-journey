import random as rd
import numpy as np
import matplotlib.pyplot as plt


#=============================================
while True:
    try:
        user_number_1 = int(input("چند روز داده میخوای بررسی کنم؟ "))
        user_number_2 = int(input("چند روز اخیر رو برای پیشبینی در نظر بگیرم؟ "))
        user_number_3 = int(input("چند عدد واقعی رو میخواید وارد کنید؟ (1 تا 30)"))
        break
    except ValueError:
        print("این عدد معتبر نیست!")
#=============================================


#=============================================
if user_number_1 <= 0:
    user_number_1 = 5
    print(f"عدد نباید منفی یا صفر باشد به صورت خودکار روی 5 روز داده جایگزین شد. . .")
#=============================================


#=============================================
if user_number_2 <= 0:
    user_number_2 = 3
    print(f"عدد نباید منفی یا صفر باشد به صورت خودکار روی 3 روز اخیر جایگزین شد. . .")
#=============================================


#=============================================
if user_number_3 > 30:
    user_number_3 = 30
    print(f"عدد بیش از حد مجاز است به صورت خودکار عدد به {user_number_3} تغییر کرد.")
elif user_number_3 <= 0:
    user_number_3 = 1
    print(f"عدد کمتر از حد مجاز است به صورت خودکار به {user_number_3} تغییر کرد.")

auto_mod = user_number_3 > 10
if auto_mod:
    print("اعداد بیش از حد هستن به صورت خودکار جایگزین می کنیم. . .")
#=============================================


#=============================================
if user_number_2 > user_number_1:
    print("تعداد روز های اخیر نمیتواند بیشتر از داده ها باشد.")
    user_number_2 = user_number_1
    print(f"به صورت خودکار انتخاب شد: {user_number_2}")
#=============================================


#=============================================
data = [34]
for i in range(user_number_1):
    x = rd.randint(1, 100)
    data.append(x)


last_numbers = data[-user_number_2:]
avg = np.mean(last_numbers).round(2)


print(f"داده های ساخته شده: {data}")
print(f"پیشبینی داده برای روز بعد: {avg}")
#=============================================


#=============================================
errors = [] 

for i in range(user_number_3):

    if auto_mod:
        real_number = rd.randint(1, 100)
    else:
        while True:
            try:
                real_number = int(input("عدد واقعی رو وارد کن: "))
                break
            except ValueError:
                print("عدد معتبر نیست!")

    data.append(real_number)
    
    last_numbers = data[-user_number_2:]
    new_avg = np.mean(last_numbers).round(2)


    error = real_number - new_avg
    error = round(error, 2)
    errors.append(error) 

    if not auto_mod:
        if error > 0:
            print(f"بیشتر از پیشبینی بود! پیشبینی: {new_avg} - خطا: {error}")
        elif error < 0:
            print(f"کمتر از پیشبینی بود! پیشبینی: {new_avg} - خطا: {error}")
        else:
            print(f"دقیق بود! پیشبینی: {new_avg}")
#=============================================


#=============================================
errors_avg = np.mean(errors).round(2)
max_error = np.max(errors)
min_error = np.min(errors)


print("= = = = = = = = = = = = = = = = = ")
print("خطا ها")
print(f"میانگین خطا ها: {errors_avg}")
print(f"نزدیک ترین پیشبینی (کمترین خطا): {min_error}")
print(f"دور ترین پیشبینی (بیشترین خطا): {max_error}")
print("= = = = = = = = = = = = = = = = = ")
#=============================================


#=============================================
plt.plot(errors)
plt.xlabel("Prediction Number")
plt.ylabel("Error Value")
plt.title("Prediction Error Trend")
plt.show()
#=============================================
