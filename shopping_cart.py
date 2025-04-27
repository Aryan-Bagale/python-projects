# Create empty lists to store the food items and their prices
foods = []
prices = []

# Initialize the total price to 0
total = 0

# Start an infinite loop to allow user to add multiple food items
while True:
    # Ask the user to enter a food name
    food = input("Enter a food to buy (q to quit): ")
    
    # If the user enters 'q' (or 'Q'), break out of the loop
    if food.lower() == "q":
        break
    else:
        # Ask the user to enter the price for the given food
        price = float(input(f"Enter the price of {food}: $ "))
        
        # Add the food name to the foods list
        foods.append(food)
        
        # Add the price to the prices list
        prices.append(price)

# After exiting the loop, print the shopping cart
print("----YOUR CART ----")

# Loop through all the items in the foods list using their index
for i in range(len(foods)):
    # Print each food item and its corresponding price
    print(f"{foods[i]}: ${prices[i]}")

# Calculate the total by summing up all the prices
total = sum(prices)

# Print the total cost formatted to 2 decimal places
print(f"Your total is: ${total:.2f}")
