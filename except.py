'''x = int(input("Enter a positive integer: "))
divisible_numbers=[]

try:
 for num in range(1, 11):
    if num % x == 0:
     divisible_numbers.append(num)
        
        
    else:
        print(f" {num} is not divisible by {x}")
except:
 print("some error has occured")

print(divisible_numbers)

x=input("enter a number:")
fact=1
try:
 for i in range(1,5):
    fact=int(x)*i
    print(fact)
except Exception as e:
  print(e)

print('but im still here')
z=input('enter a number:')
try:
 for num in range(1,8):
  b=[1,2,5,7,9,4]
  print(b[num])
except ValueError:
  print("There is a value error")
except IndexError:
  print('There is an index error')'''

def block():
  try:
    list=[4,6,8,4,5,67]
    x=int(input("Enter a number:"))
    print(list[x])
    return 1

  except:
    print("Some error has occured")
    return 0

  finally:
    print("i will be always executed")

  print('i too am always executed')

  '''but such case as in function call normal print function is not executed after try except block'''

block()

