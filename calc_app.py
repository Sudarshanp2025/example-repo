# Auto-Graded Task 17

def calculator():
    while True:  # Loop indefinitely
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operator = input("Enter the operator (+, -, *, /): ")

            if operator not in ['+', '-', '*', '/']:
                raise ValueError("Invalid operator")

            # Make computations ~ can represent operators as strings
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:     # NB ~ `if` in `elif` command.
                    raise ZeroDivisionError("Cannot divide by zero!")
                result = num1 / num2

            # Record the calculation in equations.txt. Copied as I struggle with this part.
            with open('equations.txt', 'a+', encoding='utf-8') as file:
                file.write(f"{num1} {operator} {num2} = {round(result, 2)}\n")
                print("\nYour results have been successfully stored in equations.txt")
            break  # Exit the loop after successful operation

        # Handle Exceptions, but isn't this redundant?
        except (ValueError, ZeroDivisionError) as error:
            print(f"Error: {error}")


def print_previous_equations():
    try:
        with open('equations.txt', 'r', encoding='utf-8') as file:
            equations = file.readlines()
        if equations:
            print("Previous equations:")
            for equation in equations:
                print(equation.strip())
        else:
            print("No previous equations found.")
    except FileNotFoundError:
        print("No previous equations found.")


def calc_app():
    while True:
        print("\nWelcome to the Calculator App!")
        print("1. Perform Calculation")
        print("2. Print Previous Equations")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            perform_calculation() # Mistake 
        elif choice == '2':
            print_previous_equations()
        elif choice == '3':
            break  # Exit the loop and end the program
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")


# Start the app
calc_app()

