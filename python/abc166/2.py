n, k = map(int, input().split())


temp_array = []

for _ in range(k):
  temp = input()
  [temp_array.append(i) for i in list(map(int, input().split())) if i != ""]

all_member = len(list(set(temp_array)))
print(n - all_member)