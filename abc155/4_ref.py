#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
 
# n,k = map(int,input().split())
n,k = 4,3

# a_list = np.array(list(map(int,input().split())))
a_list = np.array([3,3,-4,2])
a_list = np.sort(a_list)
 
zero = a_list[a_list == 0]
pos = a_list[a_list > 0]
neg = a_list[a_list < 0]
 
def count(x): #積がx以下になるペアの個数を返す(一旦重複は考えない)
    ans = 0
    if x >= 0:
        ans += n * len(zero)
    # a_list * pos < xだから，a_list < x/posになる個数をcountしている(pos側を固定)
    ans += np.searchsorted(a_list,x // pos, side='right').sum()
    # a_list < x // negとなる者を全ての組み合わせから抜く
    ans += (n - np.searchsorted(a_list, (-x - 1) // (-neg), side='right')).sum()
    # 同じもの2つは選べない
    ans -= np.count_nonzero(a_list * a_list <= x)
    return ans // 2
 
# 計算量：O(log INF)
left = -10 ** 18
right = 10 ** 18
while left + 1 < right:
    x = (left + right) // 2
    if count(x) >= k:
        right = x
    else:
        left = x
 
print(right)