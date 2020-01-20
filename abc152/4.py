N = int(input())


num_list = [i+1 for i in range(N)]

for number in num_list:
    tmp_str = str(number)
    tmp_str.replace(tmp_str[-1], 'X').replace(tmp_str[1], tmp_str[-1]).replace('X', tmp_str[1])