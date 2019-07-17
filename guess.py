import random

r = random.randint(1, 100)
while True:
	num = input('請猜數字: ')
	if int(num) == r:
		print('恭喜猜對了!')
		break
	elif int(num) < r:
		print('比答案小')
	elif int(num) > r:
		print('比答案大')