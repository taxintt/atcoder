import math

N, dis = map(int, input().split())
counter = 0

for i in range(N):
    temp_list = list(map(int, input().split()))
    temp_num = temp_list[0]**2 + temp_list[1]**2
    temp_dis = math.sqrt(temp_num)
    print(temp_dis)
    if temp_dis <= dis:
        counter += 1
print(counter)