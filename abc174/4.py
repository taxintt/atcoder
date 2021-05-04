n = input()
list_colors = [int(x) for x in input().split()]

# WRの順番は許容されない -> RW, RR, WW
# 1個の色を変更 or 2個の入れ替え -> どういった条件でどちらを選択するか?

i, k = 0, 1
while True:
    if list_colors[i] == "W" and list_colors[k] == "R":
        list_colors[i], list_colors[k] == "R", "W"
    if list_colors[i] == "W": # WW
        k += 1
    if list_colors[k] == "R": #RR
        i += 1
     
