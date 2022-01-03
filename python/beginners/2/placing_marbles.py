# input
# 101(int) -> 101(str) -> [1,0,1]
a = list(str(input()))

emp_dict = {"1":0,"0":0}
for ele in a:
    emp_dict[ele]+=1

print(emp_dict["1"])

