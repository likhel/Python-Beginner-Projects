from swapdicfunc import swap 

dic = {}
n = int(input("enter the value of n:"))
for i in range(1,n+1):
    k = input("enter your key:")
    v = input("enter you value:")
    dic[k]=v

swap(dic)



