import itertools

n, k = map(int, input().split())
temp_list = list(map(int, input().split()))

c = itertools.combinations(temp_list, 2)
num_list = sorted(c, key=lambda x: x[0]*x[1])

output_list = list(num_list[k-1])
print(output_list[0] * output_list[1])