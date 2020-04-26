N = int(input())

goods_list=[input() for i in range(N)]
print(len(list(set(goods_list))))