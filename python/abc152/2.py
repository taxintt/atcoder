n, m = map(str, input().split())

tmp_list = []

str_1 = n * int(m)
str_2 = m * int(n)

tmp_list.append(str_1)
tmp_list.append(str_2)

print(sorted(tmp_list)[0])