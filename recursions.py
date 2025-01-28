def factorial(n):
    
    if (n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
     
print("The answer is:")
print(factorial(1))

#fibonacci sequence

def fibonacci(n):

   if(n<=0):
       return []
   elif(n==1):
       return [0]
   elif(n==2):
       return[0,1]
   else:
       sequence=fibonacci(n-1)
       sequence.append(sequence[-1]+sequence[-2])
       return sequence

x=int(input("Enter a number whose fibonacci series is to be calculated:"))
sq=fibonacci(x)
print(sq)
print(type(sq))

