lis = [6, 100, 0, 1, 2, 4, 5, 7]

lis.sort()
print(lis)
#[0, 1, 2, 4, 5, 6, 7, 100]
#[10,11,13,14,15,16]
seq = 1
reset_seq = []
for element in range(len(lis) - 1):
    if lis[element] + 1 == lis[element + 1]:
        seq += 1 
    else:
        reset_seq.append(seq)
        seq = 1
print(max(reset_seq))