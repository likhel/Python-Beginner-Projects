a=6 #global variable
print(a)
b=8

def number():
    global b
    global a
    b=7
    a=4  #local variable
    print(a)
    print(b)
    print(f"February {a}")

number()
print(a)
#print(b) will throw error because local variable.we can make local variable global by global 
#keyword
print(b) 

