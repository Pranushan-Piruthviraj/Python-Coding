b = [20,27,45,35,66,70,79]
c = []

for element in range(len(b)):
    if b[element] > 40 and b[element]%2 != 0:
        c.append(b[element])
print(c)