import random

# Questions stored as dictionaries
questions = [
    {
        "question": "Which language is mainly used for AI and ML beginners?",
        "options": ["Python", "HTML", "CSS", "SQL"],
        "answer": "A"
    },
    {
        "question": "Which data type stores multiple items in Python?",
        "options": ["List", "Integer", "Float", "Boolean"],
        "answer": "A"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "#", "/*", "-"],
        "answer": "B"
    },
    {
        "question": "Which function is used to display output in Python?",
        "options": ["input()", "display()", "print()", "show()"],
        "answer": "C"
    },
    {
        "question": "Which keyword is used to define a function?",
        "options": ["function", "define", "def", "fun"],
        "answer": "C"
    },
    {
        "question": "What is the output of 2 ** 3?",
        "options": ["5", "6", "8", "9"],
        "answer": "C"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["String", "Boolean", "Integer", "List"],
        "answer": "B"
    },
    {
        "question": "Which loop is commonly used to iterate through a list?",
        "options": ["for", "if", "def", "try"],
        "answer": "A"
    },
    {
        "question": "Which function takes input from the user?",
        "options": ["scan()", "input()", "read()", "get()"],
        "answer": "B"
    },
    {
        "question": "Which collection stores key-value pairs?",
        "options": ["List", "Tuple", "Dictionary", "Set"],
        "answer": "C"
    }
]


# Display the question
def ask_question(question, number):

    print("\n-------------")
    print("Question", number)
    print("---------------")

    print(question["question"])

    letters = ["A", "B", "C", "D"]

    for i in range(4):
        print(f"{letters[i]}.{question['options'][i]}")

    # Input validation
    while True:

        answer = input("\nYour answer (A/B/C/D):").upper()

        if answer in ["A", "B", "C", "D"]:
            return answer

        print("Invalid choice! Please enter A, B, C or D.")


# Calculate grade
def calculate_grade(percentage):

    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


# Run quiz
def run_quiz():

    score = 0

# Create a copy and shuffle questions
    quiz_questions = questions.copy()
    random.shuffle(quiz_questions)

    print("\n==================")
    print("          PYTHON QUIZ APPLICATION")
    print("=====================")

    print("Welcome to the Python Quiz!")
    print("There are 10 questions.")
    print("Choose A, B, C or D.")

    input("\nPress Enter to start.")

    for number, question in enumerate(quiz_questions, start=1):

        user_answer = ask_question(question, number)

        if user_answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            correct_answer = question["answer"]

            print("Wrong!")
            print("Correct answer:", correct_answer)

    # Result
    total = len(quiz_questions)

    percentage = (score / total) * 100

    grade = calculate_grade(percentage)

    print("\n============")
    print("             QUIZ RESULT")
    print("===============")

    print("Correct Answers :", score)
    print("Wrong Answers   :", total - score)
    print("Total Questions :", total)
    print("Percentage      :", f"{percentage:.2f}%")
    print("Grade           :", grade)

    if percentage >= 80:
        print("\n Excellent performance!")
    elif percentage >= 50:
        print("\n Good job! Keep practising.")
    else:
        print("\n Keep learning and try again!")


# Main program
while True:

    run_quiz()

    again = input("\nDo you want to play again? (Y/N): ").upper()

    if again != "Y":
        print("\nThank you for playing!")
        break
