# Study Quiz - backup version (in case Copilot's live code doesn't work)
# Run it with:  python quiz_final.py

questions = [
    {
        "question": "What does 'cloud computing' mean?",
        "options": ["A. Computers in the sky", "B. Using computing services over the internet", "C. A type of weather software"],
        "answer": "B",
    },
    {
        "question": "What is Microsoft Foundry used for?",
        "options": ["A. Building, deploying and managing AI apps and agents", "B. Editing photos", "C. Making spreadsheets"],
        "answer": "A",
    },
    {
        "question": "In a prompt, what does the 'role' tell the AI?",
        "options": ["A. How long to answer", "B. Who it should be", "C. Which language to use"],
        "answer": "B",
    },
    {
        "question": "Where should you NEVER put an API key?",
        "options": ["A. In a .env file", "B. In a password manager", "C. In your code on GitHub"],
        "answer": "C",
    },
    {
        "question": "What does GitHub Copilot help you do?",
        "options": ["A. Write and improve code faster", "B. Book meetings", "C. Design posters"],
        "answer": "A",
    },
]

print("Welcome to Study Quiz! Type A, B or C for each question.\n")
score = 0

for number, q in enumerate(questions, start=1):
    print(f"Question {number}: {q['question']}")
    for option in q["options"]:
        print("  " + option)

    reply = input("Your answer: ").strip().upper()
    while reply not in ("A", "B", "C"):
        reply = input("Please type A, B or C: ").strip().upper()

    if reply == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Not quite. The answer is {q['answer']}.\n")

print(f"You scored {score} out of {len(questions)}.")
if score == len(questions):
    print("Perfect score! Great job!")
elif score >= 3:
    print("Well done! Keep learning.")
else:
    print("Good try! Check the Learn Plan link and try again.")
