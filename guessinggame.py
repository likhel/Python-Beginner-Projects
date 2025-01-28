
import random
def guess_game(x):

    com_num = random.randint(1,x)
    guess = 0

    while guess != com_num:

      guess = int(input(f"GUESS A NUMBER BETWEEN 1 AND {x}:"))
      if guess > com_num:
            print("Sorry, the number you guessed is high")

      elif guess < com_num:
            print("Sorry, the number you guessed is  low")
     
    print(f"Congratulations!{com_num} is a correct guess")

        

guess_game(100)


'''
def challenge(y):
    guess1 = 0
    feedback = " "
    low = 1
    high = y

    while feedback != "c":
        if low != high:
          guess1 = random.randint(low, high)
        else:
            guess1 = low

        
        feedback = input(f"Is {guess1}  too high(H), too low(L) or correct(C):").lower()
        if feedback == 'h':
            high = guess1 - 1

        elif feedback == 'l':
            low = guess1 + 1
    
    print(f"Computer has guessed the correct number {guess1}")
    ques = input("DO YOU WANT TO PLAY AGAIN(Y/N):").lower()
    if ques == "y":
        challenge(100)
    elif ques == "n":
        print('Thankyou...')


challenge(100)'''



        
