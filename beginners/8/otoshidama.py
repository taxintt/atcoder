def checker(y,a,b,c):
    if y == 10000*c + 5000*b + 1000*a:
        return True
    else:
        return False
 
def main():
    a,b,c = 0,0,0
    n,y = map(int, input().split())
 
    for i in range(n+1): 
        a = i
        for j in range(n+1):
            b = j
            c = n - i - j
            if checker(y,a,b,c):
                break
        if checker(y,a,b,c):
            break
    if a<0 or b<0 or c<0:
        a,b,c = -1,-1,-1
    print("{} {} {}".format(c,b,a))
 
 
if __name__ == "__main__":
    main()