N = int(input())

money = 0
counter = 0
while True:
    counter += 1
    money += counter
    if money >= N:
        break

print(counter)
