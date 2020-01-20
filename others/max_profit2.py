n = input()

num_list = [int(input()) for _ in range(n)]

max_int = -1
min_int = num_list[0]

for i in range(len(num_list)):
    print("num_list[i]: " + str(num_list[i]))

    max_int = max(max_int, num_list[i+1] - min_int)
    min_int = min(min_int, num_list[i+1])

    print("max_int: " + str(max_int))
    print("min_int: " + str(min_int))

print(max_int - min_int)

print(max(-1, 0))