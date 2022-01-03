# n = 3, a = [8,12,40]
n = int(input())
nums = [int(i) for i in input().split()]

ans = 0
while True:
    # リストに要素が含まれているとTrue, 空のリストはFalse
    # i % 2 == 1 の時にTrueであれば、数字がリストに含まれる
    if [i for i in nums if i % 2 == 1]:
        break
    nums = [i//2 for i in nums]
    ans += 1
print(ans)