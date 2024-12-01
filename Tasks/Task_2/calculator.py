def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))  
        except ValueError:  
            print("Invalid input. Please enter a valid number.")

def perform_calculation():
    while True:
        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter choice (1-2-3-4-5): ")

        if choice == '1':
            operation = "addition"
        elif choice == '2':
            operation = "subtraction"
        elif choice == '3':
            operation = "multiplication"
        elif choice == '4':
            operation = "division"
        elif choice == '5':
            print("Thank u for using calculator. Goodbye!")
            return  
        else:
            print("Invalid choice. Please select a valid operation.")
            continue

        while True:
            if operation == "addition":
                num1 = get_number_input("Enter first number: ")
                num2 = get_number_input("Enter second number: ")
                result = num1 + num2
                print(f"result of adding {num1} and {num2} is {result}.")
            elif operation == "subtraction":
                num1 = get_number_input("Enter first number: ")
                num2 = get_number_input("Enter second number: ")
                result = num1 - num2
                print(f"result of subtracting {num2} from {num1} is {result}.")
            elif operation == "multiplication":
                num1 = get_number_input("Enter first number: ")
                num2 = get_number_input("Enter second number: ")
                result = num1 * num2
                print(f"result of multiplying {num1} and {num2} is {result}.")
            elif operation == "division":
                num1 = get_number_input("Enter first number: ")
                while True:
                    num2 = get_number_input("Enter second number: ")
                    if num2 == 0:
                        print("Cannot divide by zero. Please enter a non-zero number.")
                    else:
                        break
                result = num1 / num2
                print(f"result of dividing {num1} by {num2} is {result}.")

            again = input("Do u want to perform another calculation? (Y/N): ").lower()
            if again != 'Y':
                print("Thank you for using calculator. Goodbye!")
                return  

            change_operation = input("Do you want to change operation? (Y/N): ").lower()
            if change_operation == 'Y':
                break 

perform_calculation()
