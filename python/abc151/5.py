import itertools

def factorial(n) : 
    M = 1000000007
    f = 1
  
    for i in range(1, n + 1):  
        f = f * i # WRONG APPROACH as  
                  # f may exceed (2^64 - 1)  
  
    return f % M  

def main():
    _, k = map(int, input().split())
    l = [int(i) for i in input().split()]

    c = itertools.combinations(l, k)

    count_for_sum = []

    for v in c:
        tmp_list = sorted(list(v))
        count_for_sum.append(tmp_list[-1] - tmp_list[0])

    print(sum(count_for_sum))

if __name__ == "__main__":
    main()