N = int(input())

nu_list = [1,4,2,3,5]

for index in range(1,N):
    current = nu_list[index]
    position = index

    while position > 0 and current > nu_list[position-1]:
        print("Swapped {} for {}".format(nu_list[position], nu_list[position-1]))
        nu_list[position] = nu_list[position-1]
        print(nu_list)
        position-=1
        print("---move position---")
    nu_list[position] = current
    print(nu_list)
    print("---loop finished---")
    print("")
print(nu_list)
