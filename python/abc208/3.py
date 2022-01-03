N, K = map(int, input().split(' '))

person_num_list = list(map(int, input().split(' ')))

count_list = [0] * len(person_num_list)

while True:
    if K - N > 0:
        count_list = list(map(lambda x: x + (K // N), count_list))
        K = K - (N * (K // N))
        continue
    elif K - N == 0:
        count_list = list(map(lambda x: x + 1, count_list))
        break
    else:
        dic = {person_num: index for index,
               person_num in enumerate(person_num_list)}
        sorted_person_num = sorted(list(dic.keys()))
        for i in range(K):
            index = dic[sorted_person_num[i]]
            count_list[index] = count_list[index] + 1
        break

[print(i) for i in count_list]