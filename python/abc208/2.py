import math
num = int(input())

counter = 0
yen_num = 10

while True:
	if yen_num == 0:
		break
	if num < math.factorial(yen_num):
		yen_num = yen_num - 1
		continue
	num = num - math.factorial(yen_num)
	counter += 1
print(counter)