import random as R

# File: kbc_questions.py

# List of KBC questions
kbc_questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "New Delhi", "Kolkata", "Chennai"],
        "correct_answer": "New Delhi"
    },
    {
        "question": "Who is known as the 'Missile Man of India'?",
        "options": ["APJ Abdul Kalam", "Vikram Sarabhai", "Homi Bhabha", "ISRO"],
        "correct_answer": "APJ Abdul Kalam"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "correct_answer": "Mars"
    },
    {
        "question": "What is the national animal of India?",
        "options": ["Lion", "Tiger", "Elephant", "Peacock"],
        "correct_answer": "Tiger"
    },
    {
        "question": "Which Indian cricketer is also known as 'The Wall'?",
        "options": ["Sachin Tendulkar", "MS Dhoni", "Rahul Dravid", "Virat Kohli"],
        "correct_answer": "Rahul Dravid"
    },
    {
        "question": "Which is the largest continent in the world?",
        "options": ["Asia", "Africa", "Europe", "Antarctica"],
        "correct_answer": "Asia"
    },
    {
        "question": "What is the full form of 'www' in a website browser?",
        "options": ["World Wide Web", "World Web Window", "Wide Web World", "Web World Wide"],
        "correct_answer": "World Wide Web"
    },
    {
        "question": "Who invented the light bulb?",
        "options": ["Alexander Graham Bell", "Nikola Tesla", "Thomas Edison", "Albert Einstein"],
        "correct_answer": "Thomas Edison"
    },
    {
        "question": "What is the square root of 64?",
        "options": ["6", "8", "10", "12"],
        "correct_answer": "8"
    },
    {
        "question": "Which gas do plants use in photosynthesis?",
        "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
        "correct_answer": "Carbon Dioxide"
    }
]
ans = ("New Delhi" , "APJ Abdul Kalam" , "Mars" , "Tiger" , "Rahul Dravid", "Carbon Dioxide" , "8" , "Thomas Edison" , "World Wide Web" , "Asia")
a = input("Do You Want To Play KBC In Python ? | Answer In Yes Or No - ")


while (a=="Yes"):
    # Printing Question for The User 
    quex = R.choice(kbc_questions)
    print(f"Question: {quex['question']}")
    for idx, option in enumerate(quex["options"], 1):
        print(f"  {idx}. {option}")

    # Taking User's Input For The Question
    # And Locking The User's Input
    try:
        user_ans = input("Enter Your Answer :")
        lock_ans = input(f"You Seleected {user_ans} , Do You Want To Lock Your Answer (Yes / No) - ")
        if user_ans in ans:
            if lock_ans=="Yes":
                print("🎉 Your answer is correct! You have won ₹10,000!")
                a = input("Would You Like To Risk Your 10000 For The Next Round (Yes / No) - ")
                if a=="No":
                    break
        else:
            if lock_ans=="Yes":
                print("I am Feeling Bad To Tell You That Your Answer Is Wrong")
                
                a = input("Would You Like To Use Your Lifeline To Play For The Next Question ( Yes / No ) - ")
                if a=="No":
                    break
    except ValueError:
        a = input("Do You Want Enter In The Next ROund Of KBC (Yes / No) - ")
        if a=="No":
            break
        


print("\nThank you for playing KBC! Goodbye!")
