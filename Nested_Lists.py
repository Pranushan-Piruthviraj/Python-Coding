a = [["apple", 5],["banana",2]]
print(len(a))
names = ["chi", "beta", "alpha"] 
scores = [20.0,50.0,50.0]
#out = [["chi", 20.0],["beta",50.0],["alpha",50.0]]

scores_tmp = scores.copy()
g = max(scores_tmp)
h = scores_tmp.count(g)
for element in range(0,h):
    scores_tmp.remove(g)
second_highest_score = max(scores_tmp)
c = []
for element in range(0,len(names)):
    d = names[element] 
    e = scores[element]
    if e == second_highest_score:
        print(d, e)
    f = []
    f.append(d)
    f.append(e)
    c.append(f)
c.sort()
print(c)
#chi
#20.0


# for element in range(0, len(scores)):
#     if scores[element] == second_highest_score:
#         print(scores[element], names[element])