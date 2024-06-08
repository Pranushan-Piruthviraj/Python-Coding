#1- I want to print all the values in a dictionary
dict_a = {"a":1, "b":2, "c":3}
for value in dict_a.values():
    print(value)

   #2- I want to find the average of all the numbers in a list
    list_a = [1, 2, 3, 4, 5]
total_sum = 0
for number in list_a:
    total_sum += number
average = total_sum / len(list_a)
print(average)

#3- I want to count to 10 -> Bonus: Can you fix the code with a break statement?
number = 1
while True:
    print(number)
    if number == 10:
        break
    number += 1