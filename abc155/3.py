N = int(input())

for_dict = {}
for _ in range(N):
    n = input()
    if n in for_dict:
        for_dict[n] += 1
    else:
        for_dict.setdefault(n, 1)

slist = sorted(for_dict.items(), key = lambda x : x[0])

for ele in slist:
  if ele[1] == max(for_dict.values()):
    print(ele[0])