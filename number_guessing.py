import random

def guess_game():
    predict = random.randint(1, 100)

    while True:
        try:
            number = int(input("Enter a number between 1 to 100: "))
            
            if number < 1 or number > 100:
                print("Please enter a number within the range 1 to 100.")
                continue

            if number < predict:
                print("Predict higher")
            elif number > predict:
                print("Predict lower")
            else:
                print("Congrats! You got it right!")
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")

guess_game()
