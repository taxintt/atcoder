HP, A = map(int, input().split())

count = 0
while HP > 0:
    HP = HP - A
    count += 1

print(count)