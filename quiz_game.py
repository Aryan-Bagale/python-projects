questions = (
    "In which year did World War II end?",
    "What is the derivative of sin(𝑥)?",
    "Which of the following sorting algorithms has the best average-case time complexity?",
    "What is the powerhouse of the cell?",
    "In object-oriented programming, what does 'inheritance' mean?"
)

options = (
    ("A. 1942", "B. 1945", "C. 1950", "D. 1939"),
    ("A. cos(x)", "B. -cos(x)", "C. tan(𝑥)", "D. −sin(𝑥)"),
    ("A. Bubble Sort", "B. Selection Sort", "C. Quick Sort", "D. Insertion Sort"),
    ("A. Ribosome", "B. Nucleus", "C. Golgi apparatus", "D. Mitochondria"),
    ("A. Copying the code from one class to another", "B. Creating multiple classes with the same name",
     "C. A class acquiring properties and methods of another class", "D. Converting one class into another")
)

answers = ("B", "A", "C", "D", "C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        print("CORRECT!")
        score += 1
    else:
        print("INCORRECT")
        print(f"Correct answer: {answers[question_num]}")
    
    question_num += 1

print("\n------------------------")
print("RESULTS")
print(f"Your score: {score}/{len(questions)}")
