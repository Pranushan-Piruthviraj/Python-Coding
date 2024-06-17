list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]
for element in range(len(list_a)):
    # print(list_a[element])
    if list_a[element] in list_b:
        print(list_a[element])

a = []
b = [10]

c = bool(a)
d = bool(b)

print((not c),(not d))

l = [1,3,4,2,7,8]
r = 0
for element in range(len(l)):
    r = l[element] + r
    print(r)

li = [2,3,5,9]
for element in range(len(li) - 1):
    if li[element] + 1 != li[element + 1]: 
        print(li[element])