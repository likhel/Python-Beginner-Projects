'''def add(a,b):
    try:
        c = int(a)+int(b)
        return c

    except Exception as e:
        return e
    
    finally:
        print("im always executed")
try:
    age = int(input("Enter your age:"))

    if age < 16:
        raise Exception("You can't drive")

except ValueError as v:
    print(v)'''

def operation(a,b):
    try:
        a = int(a)
        b = int(b)
        if isinstance(a,int) and isinstance(b,int):
          while True:
                op = input("Which operation do you want to perform(+,*,/,-) : ")
                if op == "+":
                    sum = a + b
                    print(sum)

    
                elif op == "*": 
                    pro = a * b
                    print(pro)
            
        
                elif op == "-": 
                    sub = a * b
                    print(sub)
            
       
                elif op == "/":
                   if b != 0:
                     div = round(a/b)
                     print(div)
                   else:
                     raise Exception('Zero division error') 

                ans = input("Do you want to perform other operations(Y/N):").lower()
                if ans == "n":
                    break
    except ValueError as v:
        print(f"Error : {v}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
            
    except Exception as e:
        print(e)

                
        
    
def get_input():
     x = input("Enter an integer:")
     y = input("Enter another integer:")
     operation(x,y)

get_input()     


        
   
    
    