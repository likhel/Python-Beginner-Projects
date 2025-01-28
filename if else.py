marks=int(input("Enter your marks:"))
print("Your marks is:",marks)

if(marks<27):
    print("You have failed")
elif(marks>=27):
    if(marks>=27 and marks<50):
        print("Your garde is C++")  
    elif(marks>=50 and marks<70):
        print("Your garde is B")
    elif(marks>=70 and marks<80):
        print("Your garde is B+")
    elif(marks>80 and marks<90):
        print("Your grade is A") 
    else:
        print("Your grade is A+")  
else:
    print("You were absent")        

c=8
d=8
a=7 if c>d else 0
print(a) 
print("c is greater than d") if c>d else print("d is greater than c") if c<d else print("c equals d")
        
