def get_positive_float(prompt: str) -> float:
    """Prompt the user for a valid positive float (greater than 0). Continuously asks until input is valid."""
    while True:
        try:
            val = float(input(prompt))
            if val > 0:
                return val
            print(" Please enter a number greater than zero.")
        except ValueError:
            print("Please enter a valid positive number (e.g., 1.5).")

# Gather inputs with validation
P = get_positive_float("Enter initial amount: ")
t = get_positive_float("Enter time period (in years): ")
r_pct = get_positive_float("Input annual interest rate (in %): ")
n = get_positive_float("Number of times it compounds per year: ")

# Convert rate to decimal
r = r_pct / 100

# Compute compound interest
A = P * pow(1 + r / n, n * t)

currency_symbol = "$" 

print(f"\nFinal amount after {t} years: {currency_symbol}{A:.2f}")
