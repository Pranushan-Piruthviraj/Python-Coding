menu = {"toppings": [], "drinks_sides": [], "order_type": ""}

# Available options
available_toppings = ["pepperoni", "mushrooms", "green peppers", "extra cheese"]
available_drinks_sides = ["soda", "water", "garlic bread", "salad"]

# Start the order process
Quit = input("Press Enter to start ordering, or enter q to quit: ")
while Quit != "q":
    print("Available pizza toppings:", available_toppings)
    while True:  # Nested loop for continuous input of toppings
        topping = input("Please enter your choice of pizza topping (or enter 'next' to proceed, 'q' to quit): ")
        if topping == "q":
            Quit = "q"
            break
        elif topping == "next":
            break  # Exit the toppings input loop
        elif topping in available_toppings:
            menu["toppings"].append(topping)
            topping = input("Please enter your choice of pizza topping (or enter 'next' to proceed, 'q' to quit): ")
        else:
            print("Invalid topping choice. Please choose from the available options.")
    
    if Quit == "q":
        break

    # Choose drinks or sides
    print("Available drinks/sides:", available_drinks_sides)
    while True:  # Nested loop for continuous input of drinks/sides
        drink_side = input("Please enter your choice of drink or side (or enter 'next' to proceed, 'q' to quit): ")
        if drink_side == "q":
            Quit = "q"
            break
        elif drink_side == "next":
            break  # Exit the drinks/sides input loop
        elif drink_side in available_drinks_sides:
            menu["drinks_sides"].append(drink_side)
        else:
            print("Invalid drink/side choice. Please choose from the available options.")
    
    if Quit == "q":
        break

    # Choose order type
    order_type = input("Would you like to dine in or take to go? (enter 'dine in' or 'take out', 'q' to quit): ")
    if order_type == "q":
        Quit = "q"
        break
    elif order_type in ["dine in", "take out"]:
        menu["order_type"] = order_type
    else:
        print("Invalid order type. Please enter 'dine in' or 'take out'.")
        continue

