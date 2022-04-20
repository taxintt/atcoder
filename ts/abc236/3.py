station_num, rapid_station_num = map(int, input().split()) 

startion_list = input().split()
rapid_startion_list = input().split()

for station_name in startion_list:
    if station_name in rapid_startion_list:
        print("Yes")
    else:
        print("No")