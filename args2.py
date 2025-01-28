from keywordanotherfile import getsinfo

try:
    nums = int(input("enter the number of arguments:"))

    l2 = []
    for i in range(nums+1):
        i = int(input("enter the value :"))
        l2.append(i)

    print(l2)
   
    t2 = tuple(l2)
    _,p = getsinfo(t2)
    print(p)

except Exception as e:
    print(e)