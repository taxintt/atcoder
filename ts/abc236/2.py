n = int(input())
num_list = map(int, input().split())

num_dict = {}

for number in num_list:
    if number in num_dict:
        num_dict[number] += 1
    else:
        num_dict[number] = 1

for item in num_dict.items():
    if (item[1] != 4):
        print(item[0])
        break