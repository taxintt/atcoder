a = int(input())

num_list = [int(x) for x in input().split()]
test_num = sum(num_list)

# Test case
# num_list = [8,12,40]
# num_list = [382253568,723152896,37802240,379425024,404894720,471526144]

counter = 0

while True:
    i, flag = 0, False
    for i in range(a):
        # 個別の数字が2で割り切れない場合はflag=True
        if num_list[i] % 2 != 0:
            flag = True
            break
        i += 1

    # flagが立ってない場合は全体を2で割る
    if flag:
        break
    else:
        counter += 1
        num_list = list(map(lambda x: x / 2, num_list))

print(counter)