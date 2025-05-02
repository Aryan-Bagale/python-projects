import random

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

MAX_DICE_PER_ROW = 5

while True:
    try:
        num_of_dice = int(input("🎲 How many dice?: "))
    except ValueError:
        print("❌ Please enter a valid number.")
        continue

    if num_of_dice <= 0:
        print("❌ Number must be greater than 0.")
        continue

    dice = [random.randint(1, 6) for _ in range(num_of_dice)]

    for i in range(0, num_of_dice, MAX_DICE_PER_ROW):
        row = dice[i:i + MAX_DICE_PER_ROW]
        for line in range(5):
            for die in row:
                print(dice_art[die][line], end=" ")
            print()
        print()  # Space between rows

    print(f"🎯 Total: {sum(dice)}")

    again = input("🔄 Do you want to roll again? (y/n): ").lower()
    if again != 'y':
        print("👋 Goodbye!")
        break
