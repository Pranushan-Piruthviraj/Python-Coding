#Debug the following based on the intended results

#1 I want to find out the average number of days in a month -- Bonus: can you fix this with the least changes to the code?
Jan = "Thirty one"
Feb = 28
Mar = 31
Apr = 30
May = 31
Jun = 30
Jul = 31
Aug = 31
Sep = 30
Oct = 31
Nov = 30
Dec = 31
(Jan + Feb + Mar + Apr + May + Jun + Jul + Aug + Sep + Oct + Nov + Dec) / 12

#2 I want to print a persons name, address and phone number in a formated way
first_name = "John"
last_name = "Doe"
address = "123 Elm Street"
phone = "5555555555"
print("Name: {first_name}  {last_name}\nResiding at: {address} \ncan be reached at {phone}")

#3 I want to make a list containing the values of two lists
list_a = [1,2,3]
list_b = ["4","5","6"]
list_c = list_a + list_b
print(list_c)