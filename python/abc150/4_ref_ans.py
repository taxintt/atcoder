from fractions import gcd
 
N, M = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

# 重複した値の排除
a = set(a) 
c = set()
l = 1

for ai in a:
    # gcd: 最大公約数を返す - gcd(6,4)=2
    # l *= ai // gcd(l, ai) -> l = l * ( ai // gcd(l, ai) )

    # lcm: 最小公倍数を返す - lcm(6,4)=12
    # lcm(a, b) = a * b / gcd(a, b)
    l = l * ai // gcd(l, ai) 
    if 0.5 * l > M:
        ans = 0
        break
    j = 0
    while True:
        # ビット右シフト(>>)
        if (ai >> j) % 2 == 0:
            j += 1
        else:
            c.add(j)
            break
    if len(c) > 1:
        ans = 0
        break
else:
    ans = (M + l // 2) // l
print(ans)