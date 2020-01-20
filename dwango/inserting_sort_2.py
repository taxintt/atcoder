N = int(input())

nu_list = [4,2,1,3,5]

for index in range(1,N):
    current_number = nu_list[index]
    position = index

    while position > 0 and current_number < nu_list[position-1]:
        nu_list[position] = nu_list[position - 1]
        position -= 1
    nu_list[position] = current_number
print(nu_list)