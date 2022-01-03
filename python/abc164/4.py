import itertools

N = input()
leng = len(N)

counter = 0 
num_list = [i for i in range(leng-3)]

for v in itertools.combinations(num_list,2):
    listv = list(v)
    listv[1] = listv[1] + 4
    temp_num = int(N[listv[0]:listv[1]])
    if temp_num % 2019 == 0:
      counter += 1
print(counter)