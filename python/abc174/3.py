def main():
    k = int(input())
    counter = len(str(k * 7))

    while True:
        if k % 2 == 0:
            print(-1)
            return 
        counter += 1
        temp7 = ''.join((["7"] * counter))
        if int(temp7) % k == 0:
            print(len(temp7))
            return 

if __name__ == "__main__":
    main()