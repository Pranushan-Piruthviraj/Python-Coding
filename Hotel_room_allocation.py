A = [1, 2, 3, 6, 5, 4, 4, 2, 5, 3, 6, 1, 6, 5, 3, 2, 4, 1, 2, 5, 1, 4, 3, 6, 8, 4, 3, 1, 5, 6, 2]
# B = [3,2,3,6,6,3,2,7,5,2,3,3]
# family_size = 5
room_counts = {}
for room in A:
    #print(room)
    if room in room_counts:
        room_counts[room] += 1
    else:
        room_counts[room] = 1
#print(room_counts)

#captains_room = 0
for key in room_counts.keys():
    if room_counts[key] == 1:
        captains_room = key
print(captains_room)