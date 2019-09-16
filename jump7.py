## 明7暗7的前100数字

a = 0
for i in range(1,100):
	a += 1
	if a % 7 == 0:#7 的倍数跳过
		continue
	elif a % 10 == 7:#7为尾数的跳过
		continue
	elif a // 10 == 7:#十位数是7的跳过
		continue
	print(a)
