def is_armstrong(number_string):
    power = len(number_string)
    sum = 0
    
    for digit in number_string:
        sum += int(digit) ** power
    
    if sum == int(number_string):
        print("Given number is an Armstrong number")
    else:
        print("Given number is not an Armstrong number")


is_armstrong("153")
is_armstrong("152")