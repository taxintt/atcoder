# intにキャストすることを忘れない!(基本はstrで渡されるので)
n = int(input())
input_list = [input() for i in range(n)]

print(len(set(input_list)))