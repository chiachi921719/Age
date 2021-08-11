driving = input("你有沒有開過車？ ")
if driving != "有" and driving != "沒有":
	input("只能輸入 有/沒有")
	raise SystemExit

age = input("你的年紀是？ ")
age = int(age)
if driving == "有":
	if age >= 18:
		print("你通過測驗了")
	else:
		print("奇怪你怎麼開過車？")
elif driving == "沒有":
	if age >= 18:
		print("趕快去考駕照吧！")
	else:
		print("很好，18歲以後就可以考囉！")