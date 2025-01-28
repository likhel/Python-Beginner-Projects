

'''
try:
 def getname(Name):
  print(f"your name is :{Name.upper()}")
                

 name = input("enter your name:")
 getname(name)

except TypeError as t:
  print("string cs")
from anotherfile import compose as c
try:
 num1 = int(input("enter a poitive integer:"))
 num2 = int(input("enter another poitive integer:"))
 opp = input("Enter an operator:")

 c(num1,num2,opp)

except Exception as e:
 print(e)
try:
 def compare(l1):
     print(l1)
     
     j=0
     for i in l1:
         if i>j:
             j=i
 
     print(j)
     
        

 nums = [23,56,89.45,67,33]
 compare(nums)

def com(li):
    l1 = []
    l2 = []
    for i in li:
        if i%2==0:
            l1.append(i)

        else :
            l2.append(i)

    return l1,l2

li = [40,65,88,70,50,23,77]
l3,l4 = com(li)
print(f"the even numbers are:{l3} ")
print(f"the odd numbers are:{l4} ")'''

def check(num):
    is_p = True
    for i in range(2,num):
        if num%i == 0:
            is_p = False
            break
       

    if is_p:
        print("the number is prime")
    else:
        print("the number is not prime")




a = int(input("enter a number:"))
check(a)
11






