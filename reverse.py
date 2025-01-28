'''name = "1234"
print(name[::-1])

list = [1,2,3,4,5,6,7,8]

for i in list[::2]:
    print(i)

length = int(input("enter a length:"))
breadth = int(input('enter a breadth:'))

if length != breadth:
    print('it is not a sqaure..')

else:
    print("it is a sqaure")

age1 = int(input("enter your age:"))
age2 = int(input("enter your age:"))

print("the greatest num is:",max(age1,age2))'''

age1 = int(input("enter your age:"))
age2 = int(input("enter your age:"))
age3 = int(input("enter your age:"))

print("the greatest age is:",max(age1,age2,age3))
print("the lowest age is:",min(age1,age2,age3))





