N, K = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

counter = 0
if K >= len(a):
  counter = 0
else:
  for _ in range(K):
      a.pop(-1)
  counter = sum(a)
print(counter)