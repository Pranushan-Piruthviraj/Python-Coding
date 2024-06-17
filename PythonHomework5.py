a = [-1,0,3,4,5,7,109,205,-405,707]
#Output: b = [ [-1,0], [3,4], [5,7], [109,205], [-405] ]
final_list = []
for element in range(0,len(a) - 1,2):
    # last = a[-1]
    temp_list = []
    temp_list2 = []
    temp_list.append(a[element])
    temp_list.append(a[element + 1])
    final_list.append(temp_list)
last = a[-1]
if len(a) % 2 != 0:
    temp_list2.append(last)
    final_list.append(temp_list2)

print(final_list)
   #if a[element], a[element + 1] != range(2)
    #temp_list.append
    
    #temp_list.append(a[element])
    
        
# b = [10, 3, 75, 8, 9, 0, -1, -23, 5, 7]
#Output c = [10, 75, 9, -1, 5]
