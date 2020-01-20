import math

N = input()
list_of_num = [int(x) for x in input().split()]

big_num = 10^9 + 7

prob = sum([i + 1 for i in list_of_num])/(N-1)
fact = math.factorial(N-1)

print((prob * fact) % big_num)