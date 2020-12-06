ask = input("請問你有沒有開過車?")
if ask != "有" and aks != "沒有":
    print("請輸入有/沒有開過車")
    raise SystemExit
age = input("請問你的年齡?")
age = int(age)
if ask == "有":
    if age >= 18:
        print("你通過測驗了")
    else:
        print("奇怪，你怎麼會開過車?")
elif ask == "沒有":
    if age >= 18:
        print("你可以考駕照")
    else:
        print("再過幾年就可以考駕照了")
