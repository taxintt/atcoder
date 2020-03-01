N, M = map(int,input().split())

num_dict = {1: 0, 2: 0, 3: 0}
i = 0

for _ in range(M):
    temp1, temp2 = map(int,input().split())
    if num_dict[temp1] > temp2 or temp2!=0:
    	num_dict[temp1] = temp2
    i += 1
    
if num_dict[1] == 0 and N != 1:  
    print(-1)
else:
    print("".join([str(num_dict[i+1]) for i in range(N)]))