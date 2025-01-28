n = int(input("enter the number of terms:"))
count = 0
n1,n2 = 0,1
nth = 1
while count<n:
    print(n1,end = "")
    n1,n2 = n2,nth
    nth = n1 +n2
    count+=1
