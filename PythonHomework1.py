a = "abrakadabra"
print(a[5])

p = a[0:5]
q = a[6:]
a = p + "p" + q 
print(a) 
# a[5] = "p"
# print(a)
#b = a.replace("a", "p")
#print(b)

c = a.find("a", 2, 8)
print(c)

d= "abraKAdabra"
e = d.islower()
print(e)

f = "abrakadabra"
g = f.islower()
print(g)

h = "ABRAKADABRA"
i = h.isupper()
print(i)

j = "abrakadabra"
k = j.isupper()
print(k)