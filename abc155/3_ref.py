N = int(input())

for_dict = {}

# collections.Counter(l)を使って、listにappendして一気に数え上げてもいい
for _ in range(N):
    n = input()
    if n in for_dict:
        for_dict[n] += 1
    else:
        for_dict[n] = 1

d_max = max(for_dict.values())
ans = [k for k, v in for_dict.items() if v == d_max]

for ele in sorted(ans):
    print(ele)
