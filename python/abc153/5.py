import itertools

N, M = map(int, input().split())

list_magic = []
for _ in range(M):
    a, b = map(int, input().split())
    list_magic.append({a,b})

tmp_list = list(map(lambda x: int(x.key()), list_magic))
for v in itertools.permutations(tmp_list, 2):
    print(v)