for i in range(6):
    for num in range(i):
        print(i, end="")
    print()

number = 7557
print("Given number", number)
while number > 0:
    # get the last digit
    digit = number % 10
    # remove the last digit and repeat the loop
    number = number // 10
    print(digit, end="")

print("\n")

l1 = [1,2,3]
l2 = [str(i) for i in l1]
print(int("".join(l2)))

'''str1 = ''
for i in l1:
    if isinstance(i,str):
        str1+=i

    else:
        str1+=str(i)
print(str1)'''
    
def convert(l2):
    res = int("".join(map(str,l2)))
    print(res)

l1 = [3,6,9]
convert(l1)

for i in range(0,6):
    for j in range(0, i ):
        print("*", end=' ')
    print(" ")


for i in range(6,0,-1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")




