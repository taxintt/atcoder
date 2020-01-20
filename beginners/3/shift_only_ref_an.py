# n = 3, a = [8,12,40]
n = input()
a = list(map(int, input().split()))

cnt = 0

# all(i) - 全ての要素がTrueであればTrueを返す
# i にはイテラブルオブジェクトを渡すので全ての要素を2で割り切れるか確認
while all(i%2==0 for i in a):
    a = [i/2 for i in a]
    cnt += 1

print(cnt)