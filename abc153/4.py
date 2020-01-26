N = int(input())

counter = 1
result = 0

while N!=1:
    N = N//2
    result += counter
    counter *= 2
result += counter