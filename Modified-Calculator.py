while True:
    equation = input("Give me an equation (or type 'quit' to exit): ")
    
    if equation.lower() == "quit":
        print(f"Exiting the program...")
        break
    
    try:
        first_number, operator, second_number = equation.split()
        first_number = float(first_number)
        second_number = float(second_number)
        
        if operator == "+":
            result = first_number + second_number
        elif operator == "-":
            result = first_number - second_number
        elif operator == "*":
            result = first_number * second_number
        elif operator == "/":
            if second_number == 0:
                print(f"Error: Division by zero.")
                continue
            result = first_number / second_number
        else:
            print("Invalid operator. Please try again.")
            continue
        
        print(f"Result: {result}")
    
    except (ValueError, IndexError):
        print(f"Invalid equation format. Please try again.")
        continue