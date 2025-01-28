from keywordanotherfile import getsinfo

try:
    nums = int(input("enter the number of arguments:"))

    l1 = []
    for i in range(nums+1):
        i = int(input("enter the value :"))
        l1.append(i)

    print(l1)
   
    t1 = tuple(l1)
    S,_ = (getsinfo(t1))
    print(S)

except Exception as e:
    print(e)

 
