n = 10
num1 = 0
num2 = 1
next_number = num2 
count = 1

while count <= n:
	print(num1, end=" ")
	count += 1
	num1, num2 = num2, next_number
	next_number = num1 + num2
print()

# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1

'''n = input("enter a number:")
string = n[::-1]
if string == n:
	print('your number is a palindrome')
	
else:
	print("it is not palindrome")
	
y = int(input("enter a number:"))'''

