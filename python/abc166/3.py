n, m = map(int, input().split())

height_list = list(map(int, input().split()))
# flag_list = [False * m]
road_map = {}


for i in range(m):
    # daia, daib = map(int, input().split())
    # bigger = max({daia: height_list[daia-1], daib: height_list[daib-1]})
    # smaller = min({daia: height_list[daia-1], daib: height_list[daib-1]})

    # flag_list.append(bigger)

    # if smaller in flag_list:
    #     flag_list.remove(smaller)

# print(len(list(set(flag_list))))

    daia, daib = map(int, input().split())
    if daia in road_map:
        road_map[daia].append(daib)
    else: 
        road_map.setdefault(daia, [daib])

    if daib in road_map:
        road_map[daib].append(daia)
    else: 
        road_map.setdefault(daib, [daia])
print(road_map)

tempmap = []
for i in range(m):
    templist = road_map[i+1]
    templist.append(i+1)
    biggest = max([height_list[i] for i in templist])
    tempmap[biggest] = True