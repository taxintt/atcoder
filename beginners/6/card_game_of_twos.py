n = input()

sorted_list_of_numbers = list(map(int, input().split()))
# sorted_list_of_numbers = [20,18,2,18]
sorted_list_of_numbers.sort(reverse=True)

a_sum = 0
b_sum = 0

for i, ele in enumerate(sorted_list_of_numbers):
    if i % 2 == 0:
        a_sum += ele
    else:
        b_sum += ele
print(a_sum-b_sum)