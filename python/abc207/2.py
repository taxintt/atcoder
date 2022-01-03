def main():
    a, b, c, d = map(int, input().split(' '))

    num_blue = a
    num_red = 0

    for num in range(0, 10000000):
        if num_blue <= d * num_red:
            return print(num)

        num_blue += b
        num_red += c

    print(-1)


if __name__ == '__main__':
    main()
