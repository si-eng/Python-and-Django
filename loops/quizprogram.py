# Advanced Quiz Program using Loops

questions = [
    "What is the capital of France?",
    "Which planet is known as the Red Planet?",
    "What is the largest mammal on Earth?",
    "Who wrote 'Romeo and Juliet'?",
    "What is the square root of 64?"
]

correct_answers = ["Paris", "Mars", "Blue Whale", "William Shakespeare", 8]

score = 0

print("Welcome to the Advanced Quiz Program!")

for i in range(len(questions)):
    print("\nQuestion {}: {}".format(i + 1, questions[i]))

    user_answer = input("Your answer: ")

    # Check if the answer is correct
    if user_answer.lower() == str(correct_answers[i]).lower():
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect. The correct answer is: {}\n".format(correct_answers[i]))

print("Quiz completed! Your final score is {}/{}.".format(score, len(questions)))
