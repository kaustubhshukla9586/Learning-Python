questions = ("What is the capital of India?",
            "Which planet is known as the Red Planet?",
            "How many continents are there on Earth?",
            "Which is the largest ocean in the world?",
            "Who is known as the Father of the Nation in India?",
            "Which animal is known as the Ship of the Desert?",
            "What is the largest planet in our solar system?")

options = (
    ("A. New Delhi", "B. Mumbai", "C. Kolkata", "D. Chennai"),
    ("A. Mars", "B. Jupiter", "C. Venus", "D. Saturn"),
    ("A. 5", "B. 6", "C. 7", "D. 8"),
    ("A. Atlantic Ocean", "B. Indian Ocean", "C. Pacific Ocean", "D. Arctic Ocean"),
    ("A. Mahatma Gandhi", "B. Jawaharlal Nehru", "C. Subhash Chandra Bose", "D. B. R. Ambedkar"),
    ("A. Horse", "B. Camel", "C. Donkey", "D. Elephant"),
    ("A. Earth", "B. Saturn", "C. Jupiter", "D. Neptune")
)


answers = (
    "A",  # New Delhi (Capital of India)
    "A",  # Mars (Red Planet)
    "C",  # 7 (Continents)
    "C",  # Pacific Ocean (Largest)
    "A",  # Mahatma Gandhi (Father of Nation in India)
    "B",  # Camel (Ship of the Desert)
    "C"   # Jupiter (Largest planet)
)


guesses = []
score = 0
question_num = 0
valid = ("A", "B", "C", "D")
for question in questions:
    print()
    print("----------------------------------------")
    print()
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter your chosen option(A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        print("Correct!")
        score += 1
    else:
        print()
        print("Incorrect!")
        print(f"{answers[question_num]} is the correct answer.")

    question_num += 1

print("----------------------------------------")
print("            R E S U L T S               ")
print("----------------------------------------")

print("Answers: ",end="")

for answer in answers:
    print(answer,end=" ")
print()

print("Guesses:", end=" ")


for guess in guesses:
    print(guess,end=" ")
print()

print()
score = int(score / len(questions) * 100)
print(f"Your score is {score:.2f}%")