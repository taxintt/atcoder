N, M = map(int, input().split())
list_goods = [int(x) for x in input().split()]

list_goods.sort(reverse=True)

flag = "Yes"

if list_goods[M-1] < sum(list_goods)//(4*M):
    flag = "No"

print(flag)