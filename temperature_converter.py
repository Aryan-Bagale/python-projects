unit = input("Enter temp ('C' for Celsius, 'F' for Fahrenheit, 'K' for Kelvin): ").lower()
while unit not in ('c', 'f', 'k'):
    print(f"'{unit}' is not a valid unit. Please try again.")
    unit = input("Enter temp ('C' for Celsius, 'F' for Fahrenheit, 'K' for Kelvin): ").lower()

unit_num = float(input(f"Enter the temperature value in {unit.upper()}: "))

unit_convert = input("Enter the unit you want to convert to ('C', 'F', 'K'): ").lower()
while unit_convert not in ('c', 'f', 'k'):
    print(f"'{unit_convert}' is not a valid unit. Please try again.")
    unit_convert = input("Enter the unit you want to convert to ('C', 'F', 'K'): ").lower()

if unit == 'c' and unit_convert == 'f':
    convert = (9/5) * unit_num + 32
    print(f"{unit_num}°C is {convert:.2f}°F")

elif unit == 'c' and unit_convert == 'k':
    convert = unit_num + 273.15
    print(f"{unit_num}°C is {convert:.2f}K")

elif unit == 'f' and unit_convert == 'c':
    convert = (5/9) * (unit_num - 32)
    print(f"{unit_num}°F is {convert:.2f}°C")

elif unit == 'f' and unit_convert == 'k':
    convert = (unit_num - 32) * 5/9 + 273.15
    print(f"{unit_num}°F is {convert:.2f}K")

elif unit == 'k' and unit_convert == 'c':
    convert = unit_num - 273.15
    print(f"{unit_num}K is {convert:.2f}°C")

elif unit == 'k' and unit_convert == 'f':
    convert = (unit_num - 273.15) * 9/5 + 32
    print(f"{unit_num}K is {convert:.2f}°F")

else:
    print("Invalid conversion, please try again.")
