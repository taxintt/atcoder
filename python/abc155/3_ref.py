N = int(input())

for_dict = {}

# collections.Counter(l)を使って、listにappendして一気に数え上げてもいい
for _ in range(N):
    n = input()
    if n in for_dict:
        for_dict[n] += 1
    else:
        for_dict[n] = 1

# 出現回数の最大値を取得する
d_max = max(for_dict.values())

# 最大値と一致する出現回数の文字列を抽出する
ans = [k for k, v in for_dict.items() if v == d_max]

# 辞書順にsortして出力する
for ele in sorted(ans):
    print(ele)
