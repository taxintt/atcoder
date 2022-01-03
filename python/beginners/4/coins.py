# indexを利用しないloopの場合は「 _ 」を利用することも可能
# a, b, c, coin_sum = [int(input()) for _ in range(4)]

# a, b, c, coin_sum = map(int, [input() for i in range(4)])

a = int(input()) #500 - 0
b = int(input()) #100 - 1
c = int(input()) #50 - 2

coin_sum = int(input())
counter = 0

# 全探索
for i in range(a+1): 
    for j in range(b+1):
        for k in range(c+1): # range(2+1)->loop:0~2
            if 500 * i + 100 * j + 50 * k == coin_sum:
                counter += 1
print(counter)
