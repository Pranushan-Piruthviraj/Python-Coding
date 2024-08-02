# b = [10, 3, 75, 8, 9, 0, -1, -23, 5, 7]
c = []
b = [8, 5, -1, 20, 105]

for element in range(len(b)):
    if element%2 != 0:
        c.append(b[element])
print(c)


a = [6, 9, -2, 0, 7]
a.sort()
#a = [-2, 0, 6, 7, 9]
d = len(a)

if d%2 != 0:
    mid_index = (d - 1 / 2)
    mid_number = a[mid_index]
else:
    mid_index1 = d / 2 - 1  
    mid_index2 = d / 2
    median = (a[mid_index1] + a[mid_index2]) / 2

    print(median) 

c = [-10, -23, 109, 23, 17, 9]
c.sort()
#c = [-23, -10, 9, 17, 23, 109]
e = len(c)

if e%2 != 0:
    mid_index1 = (e - 1 / 2)
    mid_number1 = c[mid_index]
else:
    mid_index2 = e / 2 - 1  
    mid_index3 = e / 2
    median2 = (c[mid_index2] + c[mid_index3]) / 2

    print(median2) 