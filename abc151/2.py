n, k, m = map(int, input().split())

point_list = [int(i) for i in input().split()]
sum_points = sum(point_list)

if m * n - sum_points > k:
    print(-1)
else:
    if m * n - sum_points < 0:
        print(0)
    else:
        print(m * n - sum_points)