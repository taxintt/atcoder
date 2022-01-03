# 各桁の和を計算して返す
# 数字を10で割った余りを加算していく
def findSumOfDigits(i):
    temp_sum = 0
    while i > 0:
        _, mod = divmod(i,10)
        temp_sum += mod
        i = i // 10
    return temp_sum
    
def main():
    n, a, b = map(int, input().split())

    # testcase
    # n, a, b = 20,2,5
    # n, a, b = 100,4,16

    for_sum = 0
    for i in range(1,n+1):
        sum_of_all_digits = findSumOfDigits(i)
        if a <= sum_of_all_digits <= b:
            for_sum+=i
    print(for_sum)

if __name__ == "__main__":
    main()
