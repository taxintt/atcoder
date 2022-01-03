temp_list = input().split()
temp_len = len(temp_list)

if temp_len - 1 == len(list(set(temp_list))):
    print("Yes")
else:
    print("No")