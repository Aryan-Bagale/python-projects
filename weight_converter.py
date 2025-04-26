def weight_converter():
    # Ask for unit until it's valid
    while True:
        weight_unit = input("Enter your weight unit ('k' for Kilograms or 'p' for Pounds): ").lower()
        if weight_unit in ('p', 'k'):
            break
        print(f"'{weight_unit}' is not a valid unit. Please try again.")

    # Ask for weight until it's a valid number
    while True:
        try:
            weight = float(input(f"Please enter your weight in {'pounds' if weight_unit == 'p' else 'kilograms'}: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    # Calculate and show result
    if weight_unit == 'p':
        converted = weight / 2.20462
        print(f" Your weight in kilograms is {converted:.2f} kg\n")
    else:
        converted = weight * 2.20462
        print(f" Your weight in pounds is {converted:.2f} lbs\n")

# Main program loop
while True:
    weight_converter()
    again = input("🔄 Do you want to convert another weight? (y/n): ").lower()
    if again != 'y':
        print("👋 Goodbye! Thanks for using the converter.")
        break
