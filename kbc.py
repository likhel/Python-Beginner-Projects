
import time
import random
 


questions=[ {
    "question":"What is capital of U.S.A ?",
    "options" :["A. Washington DC","B. Rome","C. California","D. Toronto"],
    "answer": 'A'},
    {
    "question": "Who won FIFA world cup in the year 2014 ?",
    "options" :["A. Brasil","B. Spain","C. Germany","D. Argentina"],
    "answer": "C"},

    {
    "question": "Who is the  current president of Nepal ?",
    "options" :["A. Likhil Tiwari","B. Ram Bahadur Karki ","C. Mailo","D. Ram Chandra Paudel"],
    "answer": "D"
    },
    {
    "question":"Which is the tallest Mountain in the World?",
    "options" :["A. Mt.Everest","B. Mt.Kanchanjunga","C. Mt.Rushmore","D. Fuji"],
    "answer": 'A'
    },

    {
    "question":"Who is the richest peeson in the world ?",
    "options" :["A. Bill Gates","B. Elon Musk","C. Mt.Mukesh Ammbani","D. Warren Buffet"],
    "answer": 'B'
    },

    {
    "question":"Which is the most popular sports in the world ?",
    "options" :["A. Baseketball","B. Football","C. Cricket","D. Hockey"],
    "answer": 'B'
    },

    {
    "question":"What magnitude earthquake did hit Nepal in 2072  ?",
    "options" :["A. 7.9","B. 7.5","C. 7.7","D. 7.8"],
    "answer": 'D'
    }
]

def ques():
    
    question=random.choice(questions)
    print(question["question"])
    for option in question["options"]:
        print(option)

    user_answer=input("Choose a option A/B/C/D :")    
    if user_answer==question["answer"]:
        print("correct answer")
        return True
    else:
        print("Wrong answer")
        
        
        return False
    
    



def playtime():
    print('Welcome to KBC.......')
    time.sleep(2)
    print('Get ready.....')
    time.sleep(2)
    print("Here's your first question......")

    attempts=3
    while attempts > 0:
        if ques():
            attempts-=1
            
            if attempts > 0:
                print("You have", attempts, "attempt(s) left.")
                time.sleep(1)
                print("Next question.....")
                time.sleep(2)
        else:
            print("Game over....")
            break

    print('Thank you for playing')

playtime()


            











