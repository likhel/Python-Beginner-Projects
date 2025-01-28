'''b = int(input("Enter a number whose factorial is to be:"))
fact=1
for i in range(b):
   
    fact = fact*(i+1)

print(fact)

list1 = [5,6,7,8,9]
list2 = [i**2 for i in list1 ]
print(list2)'''
import math

r = int(input("enter the radius :"))

area = round(math.pi*r**2,4)
perimeter = round(math.pi*2*r,4)
print("perimeter and area are:",perimeter,area)

list1 = [(2,3,6),(4,5,6)]

print(list1)


list3 = []

for i in list1:
    n = list(i)
    n.remove(n[-1])
    x = tuple(n)
    list3.append(x)

print(list3)
    







