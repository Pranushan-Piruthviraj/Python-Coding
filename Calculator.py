equation =input("Give me an equation:")
first_number, second_number = equation.split('+')
result = int(first_number) + int(second_number)
print(result)