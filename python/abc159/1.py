import itertools
import math


def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
  
n,m = map(int, input().split())
temp_n = combinations_count(n+m,2)
    
print(temp_n - (n*m))