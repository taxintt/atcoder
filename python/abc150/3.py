import itertools

n = int(input())

p_list = [int(i) for i in input().split()]
q_list = [int(i) for i in input().split()]

num_list = [i+1 for i in range(n)]

a = 0
b = 0

for i, v in enumerate(itertools.permutations(num_list, n)): 
    if(list(v) == p_list):
        a = i
    if(list(v) == q_list):
        b = i
print(abs(a - b))