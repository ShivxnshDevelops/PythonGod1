import random as R

# File: kbc_questions.py

# List of KBC questions
kbc_questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "New Delhi", "Kolkata", "Chennai"],
        
    },
    {
        "question": "Who is known as the 'Missile Man of India'?",
        "options": ["APJ Abdul Kalam", "Vikram Sarabhai", "Homi Bhabha", "ISRO"],
        
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        
    },
    {
        "question": "What is the national animal of India?",
        "options": ["Lion", "Tiger", "Elephant", "Peacock"],
        
    },
    {
        "question": "Which Indian cricketer is also known as 'The Wall'?",
        "options": ["Sachin Tendulkar", "MS Dhoni", "Rahul Dravid", "Virat Kohli"],
        
    }
]
ans = ("New Delhi" , "APJ Abdul Kalam" , "Mars" , "Tiger" , "Rahul Dravid")
a = input("Do You Want To Play KBC In Python ? | Answer In Yes Or No - ")


while (a=="Yes"):
    # Printing Question for The User 
    quex = R.choice(kbc_questions)
    print(f"Question: {quex['question']}")
    for idx, option in enumerate(quex["options"], 1):
        print(f"  {idx}. {option}")

    # Taking User's Input For The Question
    try:
        user_ans = input("Enter Your Answer :")
        lock_ans = input(f"You Seleected {user_ans} , Do You Want To Lock Your Answer (Yes / No) - ")
        if user_ans in ans:
            if lock_ans=="Yes":
                print("🎉 Your answer is correct! You have won ₹10,000!")
                a = input("Would You Like To Risk Your 10000 For The Next Round (Yes / No) - ")
            else:
                a = input(" Your Answer Is Incorrect \nDo You Want Enter In The Next Round Of KBC (Yes / No)")
        else:
            a = input("Do You Want Enter In The Next ROund Of KBC (Yes / No - ")
    except ValueError:
        a = input("Do You Want Enter In The Next ROund Of KBC (Yes / No) - ")
        
    # Locking The User's Input 
    

    # if lock_ans=="Yes":
    #     if user_ans in ans:
    #         print("🎉 Your answer is correct! You have won ₹10,000!")
    #         a = input("Do You Want Enter In The Next ROund Of KBC (Yes / No)")
            
    #     else:
    #         print(f"❌ Sorry, Your answer is wrong. ")
    #         a = input("Do You Want Enter In The Next ROund Of KBC (Yes / No)")


print("\nThank you for playing KBC! Goodbye!")
