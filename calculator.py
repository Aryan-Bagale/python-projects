def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculator():
    while True:
        operator = input("Enter an operator (+, -, *, /): ")

        while operator not in ('+', '-', '*', '/'):
            print("You entered a wrong operator, please try again.")
            operator = input("Enter an operator (+, -, *, /): ")

        num1 = get_number("Enter your 1st number: ")
        num2 = get_number("Enter your 2nd number: ")

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = round(num1 / num2, 2)
            else:
                print("Error: Division by zero!")
                continue  # Skip to the next loop

        print(f"The result is: {result}")

        again = input("Do you want to perform another calculation? (y/n): ").lower()
        if again != 'y':
            print("Thanks for using the calculator. Goodbye!")
            break

# Run it
calculator()
