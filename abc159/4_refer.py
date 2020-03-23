import collections

length = int(input())
temp_list = list(map(int, input().split()))

all_count = 0
c = collections.Counter(temp_list)

for i in c.values():
    # nCrの実装(r=2の時) ... (1)
    # -> n! / 2! * (n-2)! = n * (n-1) / 2
    ans += i*(i-1)//2

for x in range(length):
    # k番目のボールの値(temp_value)を取得して、同じ数字のボールの数を数える
    temp_value = temp_list[x]
    count = c[temp_value]

    # 最終的にパターンの数がどのように変わるか確認すると、n * (n-1) / 2を引いて、 n-1 * (n-2) / 2を足すので【-n+1】が変化量となる((1)を参照)
    # (1,1,2,1,2)でk=2とすると、1については -3C2 / +2C2 となる
    print(ans - count + 1)