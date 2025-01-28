pw=(input("enter you pw:"))
if(len(pw)>7 and len(pw)<20):
    print(pw)
elif(len(pw)<7):

    raise ValueError("your characters are insufficient")

else:
    raise ValueError("your characters are too long")

pw=(input("enter you PW:"))
if(pw=="quit"):
    print(pw)
else:
   raise ValueError("INCORRECT PASSWORD")