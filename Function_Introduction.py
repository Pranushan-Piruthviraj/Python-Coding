# def user_input(isCount = False):
#     current_weather = input("How is the weather today?: ")
#     print(current_weather)
#     if isCount == True:
#         print(len(current_weather))

# print("Now we are printing without count")
# user_input()
# print("Now we are printing with count")
# user_input(True)

# def user_input(First_Name = "Pranushan",Last_Name = "Piruthviraj"):
#     print("First name is: ", First_Name)
#     print("Last name is: ", Last_Name)

# print("Now we are printing user info")
# user_input("Pranushan")


# def sum_alpha_scaling(num_1,num_2,scaling_factor):
#     s  = (num_1 + num_2) * scaling_factor
#     return s

# d = sum_alpha_scaling(num_2 = 2, num_1 =  3,scaling_factor =  5)
# print(d)
# build_dict = {}
# def build_dictionary(key,value):

#     build_dict[key] = value
#     #return build_dict
#     return build_dict.copy()


# d = build_dictionary("Name", "Pranushan")
# print(d)
# e = build_dictionary("Last", "Piruthviraj")
# print(type(e))
# print(d)

def user_name(name):
    print("Hey you inserted name: ", name)

while True:
    a = input("Enter your name  (press q to quit): ")
    if (a == "q"):
        break
    else:
        user_name(a)