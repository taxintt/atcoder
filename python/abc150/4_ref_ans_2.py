def d_semi_common_multiple():
    from fractions import gcd
    from functools import reduce
    N, M = [int(i) for i in input().split()]
    A = [int(i) // 2 for i in input().split()]  # 先に2で割っておく
 
    def count_divide_2(n):
        ret = 0
        while n % 2 == 0:
            ret += 1
            n //= 2
        return ret
 
    def lcm(a, b):
        return a * b // gcd(a, b)
 
    # A の全要素について、2で割れる回数は等しいか？
    tmp = count_divide_2(A[0])
    for a in A:
        if count_divide_2(a) != tmp:
            return 0
 
    t = reduce(lambda x, y: lcm(x, y), A)
    return M // t - M // (2 * t)
 
print(d_semi_common_multiple())