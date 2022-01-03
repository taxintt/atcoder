import itertools


# origin_list = [100,50,50]
origin_list = []

a = int(input())
origin_list.extend([500]*a)

b = int(input())
origin_list.extend([100]*b)

c = int(input())
origin_list.extend([50]*c)

number = int(input())

counter = 0
tmp_list = []

for i in range(len(origin_list)):     
    for j in itertools.combinations(origin_list, r=i): 
        if sum(j) == number:
            tmp_list.append(j)
origin_list = list(set(tmp_list))
print(len(origin_list))

    