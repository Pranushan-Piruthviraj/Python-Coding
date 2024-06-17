x = 1
y = 2
n = 2   

final_output = []
for element in range(x + 1):
    for element2 in range(y + 1):
        temp_list = []
        if element + element2 != n:
            temp_list.append(element)
            temp_list.append(element2)
            final_output.append(temp_list)
print(final_output)


