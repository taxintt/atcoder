n = input()

num_list = [int(input()) for _ in range(n)]

bet_list = []

for i in range(len(num_list)-1):
    if(num_list[i+1] - num_list[i] >= 0):
        bet_list.append(num_list[i+1] - num_list[i])
        # bet_list.append([i,num_list[i+1] - num_list[i]])
    else:
        continue

slist = sorted(bet_list, reverse=True) 
print(slist[0])

# bet_dict = dict(bet_list)
# slist = sorted(bet_dict.items(), key=lambda x: x[1], reverse=True)
# print(slist)

