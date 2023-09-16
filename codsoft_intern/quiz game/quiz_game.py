quiz_questions = [
    {
        'question': 'What is the capital of France?',
        'choices': ['a. London', 'b. Madrid', 'c. Paris'],
        'correct_answer': 'c'
    },
    {
        'question': 'Which planet is known as the Red Planet?',
        'choices': ['a. Venus', 'b. Mars', 'c. Jupiter'],
        'correct_answer': 'b'
    },
    # Add more questions here
]

score = 0

print("Welcome to the Quiz Game!")
print("You'll be asked a series of multiple-choice questions.")
print("Choose the correct answer by entering the corresponding letter (e.g., 'a', 'b', 'c').")

for i, question in enumerate(quiz_questions, start=1):
    print(f'\nQuestion {i}: {question["question"]}')
    for choice in question['choices']:
        print(choice)
    
    user_answer = input("Your answer: ").strip().lower()

if user_answer == question['correct_answer']:
    print("Correct!")
    score += 1
else:
    print(f"Incorrect. The correct answer is {question['correct_answer'].upper()}.")

print(f'\nYour final score: {score}/{len(quiz_questions)}')

play_again = input("Do you want to play again? (yes/no): ").strip().lower()

if play_again == 'yes':
    # Reset the score and play again
    score = 0
else:
    print("Thank you for playing!")

while True:
    # Game logic here

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()

    if play_again != 'yes':
        print("Thank you for playing!")
        break
