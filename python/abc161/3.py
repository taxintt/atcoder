N, K = map(int, input().split())

amari = N%K

if amari > K//2:
    print(abs(amari - K))
else:
    print(abs(amari))