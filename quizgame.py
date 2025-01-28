questions = {"WHO IS THE CURRNET PRESIDENT OF NEPAL:?":"A",
                "WHAT IS THE BEST RATED SERIES OF ALL TIME:?":"A",
                "WHO WON THE FOOTBALL WORLD CUP IN 2010:?":"C",
                "WHO IS THE MOTHER IN HOW I MET YOUR MOTHER:?":"B"}

options = [["A.Ram Chandra Adhikari","B.KP oli","C.Likhil Dai","D.Pushpa Kamal Dahal"],
            ["A.Game of thrones","B.Breaking Bad","C.Prision Break","D.Modern family"],
            ["A.Brazil","B.France","C.Spain","Germany"],
            ["Tracy","Robin","C.Lily","D.Stella"]]



def new_game():
    

    guesses = []
    correct_guesses = 0
    question_num = 1
    
    for key in questions:
        print("************************************")
        print(key)
        for option in options[question_num-1]:
            print(option)
        guess = input("Enter (A,B,C or D):").upper()
        guesses.append(guess)
        question_num += 1
        correct_guesses += check_answers(questions.get(key),guess)

    check_score(correct_guesses,guesses)
    play_again()


def check_answers(answer,choice):
    if answer == choice:
        print("Right Answer!!")
        return 1
    else:
        print("Wrong Answer!!")
        return 0

def check_score(correct_guesses,guesses):
    print("The results are:")
    print("Guesses:",end=" ")
    for i in guesses:
        print(i,end=" ")
    print()
    print("Answer:",end=" ")
    for i in questions:
        print(questions.get(i),end=" ")
    print()

    score = correct_guesses/len(questions)*100
    print("Final score:"+str(score)+"%")



def play_again():
    while True:
        again = input("Do you want to play again? (yes/no):").upper()
        if again == "YES":
            new_game()
        elif again != "NO":
            break
        else:
            print("Please enter a valid option (yes/no)")



new_game()


    
    
