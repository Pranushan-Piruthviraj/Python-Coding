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

# def user_name(name):
#     print("Hey you inserted name: ", name)

# while True:
#     a = input("Enter your name  (press q to quit): ")
#     if (a == "q"):
#         break
#     else:
#         user_name(a)
unprinted_designs = ["phone_case", "robot_pendant", "ron"]
completed_models = []
a = 3
completed_models_tuple = ()
def list_manipulation(unprinted_designs_input, completed_models_input, a_input, completed_models_tuple_input):
    # while unprinted_designs_input:
    #     current_design = unprinted_designs_input.pop()
    #     completed_models_input.append(current_design)
    # a_input and completed_models_tupel_input are immutable data types so they dont get updated after the call
    a_input = 0
    completed_models_tuple_input = ("phone_case")
    # This will break the shallow copy of completed_models as we are instantiating a new list object for 
    # for completed_models_input. If you comment the following line shallow copy is prevented and so the 
    # input completed_models list also gets modified outisde of the function scope as 
    # completed_models_input adress is the same as completed_models
    completed_models_input = ["phone_case"]
    completed_models_input.append("ron")
def show_completed_models(completed_models_input):
    for completed_model in completed_models_input:
        print(completed_model)

#list_manipulation(unprinted_designs_input=unprinted_designs, completed_models_input=completed_models, a_input=a,completed_models_tuple_input=completed_models_tuple)
#print(a)
#print(completed_models)
#print(completed_models_tuple)
#show_completed_models(completed_models_input=completed_models)

def take_toppings(sauce, *toppings, number_of_toppings):
    #print(type(toppings))
    print(toppings)
    #print(type(number_of_toppings))
    print(number_of_toppings)
    print(sauce)
    

# take_toppings("mushrooms")
# take_toppings("extra cheese", "tomatoes", "potatoes")
#take_toppings("extra cheese", "tomatoes", "potatoes", number_of_toppings=[10,20,30]) 
# c = [30,40,50]
# print(*c)
# l = [10,20,*c]
# print(l)
def take_toppings_price(sauce, number_of_toppings, **toppings_price):
    #print(type(toppings))
    print(toppings_price)
    #print(type(number_of_toppings))
    print(number_of_toppings)
    print(sauce)

#take_toppings_price("tomato", 1, topping_1= "mushrooms", topping_1_price= 0.50)


def args_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)

#args_kwargs("Toronto", "Stouffville", province="Ontario", country="Canada")


