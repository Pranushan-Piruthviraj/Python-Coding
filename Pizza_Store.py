menu = {"toppings": [], "drinks_sides": [], "order_type": ""}

available_toppings = ["pepperoni", "mushrooms", "green peppers", "extra cheese"]
available_drinks_sides = ["soda", "water", "garlic bread", "salad"]

Quit = input("Press Enter to start ordering, or enter q to quit: ")
while Quit != "q":
    print("Available pizza toppings:", available_toppings)
    while True:  
        topping = input("Please enter your choice of pizza topping (or enter 'next' to proceed, 'q' to quit): ")
        if topping == "q":
            Quit = "q"
            break
        elif topping == "next":
            break  
        elif topping in available_toppings:
            menu["toppings"].append(topping)
        else:
            print("Invalid topping choice. Please choose from the available options.")
        #if Quit == "q":
            #break
    print("Available drinks/sides:", available_drinks_sides)
    while True:  
        drink_side = input("Please enter your choice of drink or side (or enter 'next' to proceed, 'q' to quit): ")
        if drink_side == "q":
            Quit = "q"
            break
        elif drink_side == "next":
            break  
        elif drink_side in available_drinks_sides:
            menu["drinks_sides"].append(drink_side)
        else:
            print("Invalid drink/side choice. Please choose from the available options.")
        #if Quit == "q":
            #break
    while True:
        order_type = input("Would you like to dine in or take to go? (enter 'dine in' or 'take out', 'q' to quit): ")
        if order_type == "q":
            Quit = "q"
            break
        elif order_type == "dine in" or order_type == "take out":
            menu["order_type"] = order_type
            break  
        else:
            print("Invalid order type. Please enter 'dine in' or 'take out'.")

        #if Quit == "q":
            #break
    break
print("Your current order: " , "Toppings:", menu["toppings"] , "Drinks/Sides:", menu["drinks_sides"] , "Order Type:", menu["order_type"])
           