

'''str1 = "mango-banana-cherry-apple878"



def sort(a):
    l1 =  str1.split("-")
    n = len(l1)
    for i in range(n):
       for j in range(0,n-1-i):
          if l1[j]<l1[j+1]:
           l1[j],l1[j+1] = l1[j+1],l1[j]
    print(n)

    print(l1)

sort(str1)'''

# Python3 code to demonstrate
# conversion of number to list of integers
# using list comprehension

# initializing number
num = 2019

# printing number
print("The original number is " + str(num))

# using list comprehension
# to convert number to list of integers
res = [int(x) for x in str(num)]

# printing result
print("The list from number is ", res)


        
