N = int(input())
num_list = list(map(int, input().split()))

counter = {"check": 1}

for i in range(1,N):
    if min(num_list[:i]) > num_list[i]:
        counter["check"] += 1
    

print(counter["check"])