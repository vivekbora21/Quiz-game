print("---Welcome to Python Quiz---\n")
def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A, B, C, or D): ").upper()
        if answer == question["answer"]:
            print("Correct! +1 points\n")
            score += 1
        else:
            print("Wrong! The correct answer was", question["answer"], "\n")
    print(f"You got {score} out of {len(questions)} questions correct.")

questions = [
    {
        "prompt": "Which of the following types of loops are not supported in Python?",
        "options": ["A. for", "B. while", "C. do-while", "D. None of the above"],
        "answer": "C"
    },
    {
        "prompt": "In which language is Python written?",
        "options": ["A. C++", "B. C", "C. Java", "D. None of these"],
        "answer": "B"
    },
    {
        "prompt": "WIn which language is Python written?",
        "options": ["A. Wick van Rossum", "B. Rasmus Lerdorf", "C. Guido van Rossum", "D. Niene Stom"],
        "answer": "C"
    },
    {
        "prompt": "Which keyword is used for function in Python language?",
        "options": ["A. Function", "B. def", "C. Fun", "D. Define"],
        "answer": "B"
    },
    {
        "prompt": "Which of the following is not a core data type in Python programming?",
        "options": ["A. Class", "B. Lists", "C. Tuples", "D. Dictionary"],
        "answer": "A"
    },
    {
        "prompt": "Which of the following statements is used to create an empty set in Python?",
        "options": ["A. ()", "B. []", "C. {}", "D. set()"],
        "answer": "D"
    },
]

run_quiz(questions)