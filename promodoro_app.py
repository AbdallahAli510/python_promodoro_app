import time

print("|⌛ Welcome In The Promodoro Timer !\n")

minutes = int(input("\nPlease Enter Time In Minutes: "))

print("\n")

# تحويل الدقايق الي ثواني

T_second = minutes * 60  # 2*60 = 120 sec

while T_second > -1:
    # بنجيب عدد الدقايق ك عدد صحيح بدون كسور
    min = T_second // 60

    # باقي الثواني لو فيه
    sec = T_second % 60

    # اظهار شكل التايمر 02:23
    clock = f"{min:02d}:{sec:02d}"
    # طباعة الشكل وكمان يكون علي نفس السطر
    print(f"\r ⏰ Time Remaining : {clock}", end="")

    # ننقص  ثانية ونطبع
    time.sleep(1)

    # نقلل الثواني
    T_second -= 1

print("\n\nTime Out, Take a Break 🙃 😁")
