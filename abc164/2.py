thp, tat, ahp, aat = map(int, input().split())

while True:
    ahp = ahp - tat
    thp = thp - aat
    if ahp <= 0:
        print("Yes")
        break
    elif thp <= 0:
        print("No")
        break
    else:
        continue