'''n = int(input("enter the number of objects:"))
r = int(input("enter the number to select:"))

def permut(N,R):
    fact = 1
    for i in range(1,N+1):
        fact = fact*i
    fact2 = 1
    for i in range(1,R+1):
        fact2 = fact2*i
    
    Rr = N-R
    permutation = 0
    combination = 0
    fact1 = 1
    for i in range(1,(N-R)+1):
        fact1 = fact1*i

    permutation = round(fact/fact1)
    combination = round(fact/(fact1*fact2))

    print(permutation,combination)


permut(n,r)'''

n = int(input("enter the number of objects:"))
r = int(input("enter the number to select:"))

def fctrl(a):
    fact = 1
    for i in range(1,a+1):
        fact = fact * i 
    
    return fact

N = fctrl(n)
R  = fctrl(r)
diff = n-r
D = fctrl(diff)
print("Permutation: ", round(N/D))
print("Combination: ", round(N/(R*D)))



    

        
