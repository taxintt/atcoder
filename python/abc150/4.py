n, max_num = map(int, input().split())
 
num_list = list(map(int, input().split()))
ans_list = []
 
for i in range(len(num_list)):
    p = 0
    tmp_list = []
    while max_num > num_list[i]//2 * (2*p + 1):
        tmp_list.append(num_list[i]//2 * (2*p + 1))
        p += 1
   
    if i == 0:
       ans_list = tmp_list
    else:
       ans_list = list(set(ans_list) & set(tmp_list))
print(len(ans_list))