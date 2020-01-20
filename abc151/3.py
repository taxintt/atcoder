n, m = map(int, input().split())

input_list = [set(input().split()) for _ in range(m)]
total_count_wa, total_count_ac= 0, 0

for i in range(n):
    count_wa, count_ac, tmp_index= 0, 0, 0

    tmp_list = [ele[1] for ele in input_list if int(ele[0]) == i+1]
    if "AC" in tmp_list:
      tmp_index = tmp_list.index("AC")
      total_count_ac += 1
    total_count_wa += tmp_list[:tmp_index].count('WA')
    
print(total_count_ac, total_count_wa)
    