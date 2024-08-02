dictionary = {"fruit": [], "vegetable": [], "dairy": []}
Quit = input("Press Enter to start, or enter q to quit: ")
while Quit != "q":
    grocery_items = input("Please enter the vegetable,fruit or dairy product to buy (or enter q to quit): ")
    if grocery_items == "q":
        Quit = "q"
        break
    else:
        
        product_type = input("Is this item a vegetable, fruit or dairy product? (or enter q to quit): ")
    if product_type == "q":
            Quit = "q"
            break
    else:
        dictionary[product_type].append(grocery_items)
print(dictionary)
