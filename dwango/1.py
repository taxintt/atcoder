num_of_songs = int(input())
all_list = [input().split() for _ in range(num_of_songs)]

song_name = input()
ind = 0

for i, tmp_list in enumerate(all_list):
  if tmp_list[0] == song_name:
    ind = i

if ind != len(all_list) - 1:
  print(sum([int(tmp_list[1]) for tmp_list in all_list[ind+1:]]))
else:
  print(0)