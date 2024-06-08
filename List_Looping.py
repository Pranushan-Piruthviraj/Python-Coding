# b = ["apple", "banana", "kiwi", "cherry"]
# for element in range(2,4):
#     print(b[element])
# for element in b[2:4]:
#     print(element)

# c = b[1:3]
# print(c)

a = [2,3,6,6,5]
b = max(a)
l = []
for element in a:
    if element != b:
        l.append(element)
# print(max(l))


c = a.count(max(a))
for idx in range(c):
    a.remove(max(a))
# print(max(a))

a = [30, 40, 30]
b = [10, 70, 20]
average = []
for element in range(0,3):
    average.append((a[element] + b[element]) / 2)
print(average)