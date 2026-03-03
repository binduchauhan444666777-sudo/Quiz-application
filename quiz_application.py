
print("* Welcome to our Quiz Application *")

c = input("TYPE START TO START THE QUIZ: ")

if c.lower() != "start":
    print("Quiz not started")
    exit()

print("* YOU HAVE SUCCESSFULLY STARTED THE QUIZ *")

score = 0

questions = [
    {
        "q": [
            "Q1. Who invented zero?",
            "a) Ramanujan",
            "b) Aryabhatta",
            "c) Archimedes",
            "d) Brahmagupta"
        ],
        "ans": "b"
    },
    {
        "q": [
            "Q2. Who wrote the national anthem of India?",
            "a) Mahatma Gandhi",
            "b) Rabindranath Tagore",
            "c) Subhash Chandra Bose",
            "d) Sarojini Naidu"
        ],
        "ans": "b"
    },
    {
        "q": [
            "Q3. Who is the President of India?",
            "a) Draupadi Murmu",
            "b) Nayab Singh Saini",
            "c) Manmohan Singh",
            "d) Ram Nath Kovind"
        ],
        "ans": "a"
    },
    {
        "q": [
            "Q4. Which planet is known as the Red Planet?",
            "a) Mercury",
            "b) Venus",
            "c) Mars",
            "d) Earth"
        ],
        "ans": "c"
    },
    {
        "q": [
            "Q5. Which language is mainly used for web development?",
            "a) HTML",
            "b) Python",
            "c) C",
            "d) Java"
        ],
        "ans": "a"
    }
]

for ques in questions:
    for line in ques["q"]:
        print(line)

    ans = input("Enter your answer: ").lower()

    if ans == ques["ans"]:
        print("* Correct Answer *")
        score += 1
    else:
        print("* Wrong Answer *")

    if score == 5:
        print("** AMAZING !! YOU SCORED A PERFECT SCORE OF 5/5 **")
    else:
        print("🎉 Your final score is:", score,"/ 5")



