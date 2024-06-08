a = []
print(len(a))
b = list()
print(len(b))
b.append("day")
print(b)
b.append(5)
print(b)
b.append("morning")
print(b)
# b = [0:2]
print(b[-1])
print(type(b[-1]))
print(b[0:2])
print(b[-2:])
c = b[-1]
print(c)
c = c.swapcase()
print(c)
print(b)
b[-1] = c
print(b) 
print(len(b))

e = ["hey", "day"]
g = ["apple", "mango"]
print(e + g)
f = e + g 
print(f)
# f[4] = "carrot"
f.insert(2,"carrot")
print(f)
# a = "hey"
# print(a[0])
# print(a[0:2])
# print(a[-1])
l = f
# h = f.clear()
# print(h)
i = l.pop(2)
print(i)
print(l)
l.append('apple')
print(l)
l.remove("apple")
print(l)
r = [5, -1, 1000]
# r.sort(reverse=True)
p = sorted(r)
print(p)
print(r)
r.reverse()
print(r)
# print(r[5])
a = ["cherry", "orange", "apple", "mango"]
a[0] = a[0].upper()

print(a)
for element in a:
    print(element.upper())
    print(element)
c = "sunday"
for element in c:
    print(element)
d = [0,1,2,3,4,5]
# for element in d:
#     print(element)
e = ["sunday",3,5,"carrot"]
for element in range(0,2):
    print(e[element])
# e = "saturday"
# print(e * 1000)
for element in range(0,4):
    print(a[element] * 2)
for element in d:
    print(element >= 3)
for element in d:
    d[element] = element **2
print(d)
h = [2,5,6,7]
for element in range(0,4):
     print(element)
     h[element] = element **2
     print(h)
# print(min(h))
# print(max(h))
# print(sum(h))

