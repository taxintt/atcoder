A1=list(map(int,input().split()))
A2=list(map(int,input().split()))
A3=list(map(int,input().split()))
temp_list = []
temp_list.append(A1)
temp_list.append(A2)
temp_list.append(A3)

bingo_list = [[0 for i in range(3)] for j in range(3)]

N = int(input())
for _ in range(N):
    temp = int(input())
    if (temp in A1):
      bingo_list[0][A1.index(temp)] = 1
    if (temp in A2):
      bingo_list[1][A2.index(temp)] = 1
    if (temp in A3):
      bingo_list[2][A3.index(temp)] = 1

if sum(bingo_list[0]) == 3 or sum(bingo_list[1]) == 3 or sum(bingo_list[2]) == 3 or (bingo_list[0][0]+(bingo_list[1][0])+(bingo_list[2][0])) == 3 or (bingo_list[0][1]+(bingo_list[1][1])+(bingo_list[2][1])) == 3 or (bingo_list[0][2]+(bingo_list[1][2])+(bingo_list[2][2])) == 3:
    print("Yes")
elif (bingo_list[0][0]+(bingo_list[1][1])+(bingo_list[2][2])) == 3 or (bingo_list[0][2]+(bingo_list[1][1])+(bingo_list[2][0])) == 3:
    print("Yes")
else:
    print("No")