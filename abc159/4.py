import math
import collections
from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

length = int(input())
temp_list = list(map(int, input().split()))

for i in range(length):
    tm = temp_list[:]
    tm.pop(i)
    
    c = collections.Counter(tm)
    print(sum([cmb(p, 2) for p in c.values() if p>1]))