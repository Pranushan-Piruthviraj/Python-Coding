letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

pattern = []

for index in range(len(letters)):
    row = ''
    for dash in range(len(letters) - index - 1):
        row += '--'
    for order in range(len(letters) - 1, len(letters) - index - 2, -1):
        row += letters[order]
        if order != len(letters) - index - 1:
            row += '-'
    for order in range(len(letters) - index, len(letters)):
        row += '-' + letters[order]
    for dash in range(len(letters) - index - 1):
        row += '--'
    pattern.append(row)
for index in range(len(letters) - 2, -1, -1):
        pattern.append(pattern[index])
for row in pattern:
        print(row)      