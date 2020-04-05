N, M = map(int, input().split())
list_goods = [int(x) for x in input().split()]

total = sum(list_goods)
list_goods.sort(reverse=True)

flag = "Yes"

# 割り切れないケースも考慮して / で計算
if list_goods[M-1] < total/(4*M):
    flag = "No"

print(flag)