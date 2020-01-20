n, a, b = map(int, input().split())
ans = 0

for i in range(n+1):
    # usage - map(func(), list_object)
    # 各桁の足し算: 25(int) -> 25(str) -> [2,5] -> 7
    if a <= sum(list(map(int, list(str(i))))) <= b:
        ans += i

print(ans)