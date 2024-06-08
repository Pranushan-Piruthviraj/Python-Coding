#Debug the following based on the intended results
THE_LIST = [1,2,3,4,5,6,7,8,9,10]

#1 I want to remove the third element in the list
del THE_LIST[2]
print(THE_LIST)

#2 I want to add the number 11 to the end of the list
THE_LIST.append(11)

THE_DICTIONARY = {"name": "John Doe", "address": "123 Elm Street", "phone": "5555555555"}

#3 I want to print the name, address and phone number in a formatted way
print(f"Name: {THE_DICTIONARY['name']}\nResiding at: {THE_DICTIONARY['address']}\ncan be reached at {THE_DICTIONARY['phone']}")

#4 I want to add the key value pair "age": 30 to the dictionary
THE_DICTIONARY["age"] = 30

#5 I want to make a list that can't be changed
a_list_that_cant_be_changed = (1,2,3,4,5,6,7,8,9,10)
try:
    a_list_that_cant_be_changed[0] = 10
except:
    print("This list can't be changed -- GOOD JOB!")