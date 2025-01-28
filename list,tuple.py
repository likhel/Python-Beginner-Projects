list=["likhil",'777','DAI','999','8','00','42','6',3,1]
print(list, sep='&' )
print(list[0])
print(len(list))
if "777" in list:
    print("yes")
else:
    print("no")
    
if "lI" in "likhil":
  print("yes")
else:
   print("no")

print(list[1:4])
print(list[1:5:3])
print(list[1:])

list2=[[i//2 for i in range(10) ]]
print(list2)

list3=[ i/2 for i in range(20) if i%2==0]
print(list3)
list5=[ i**2 for i in range(10) if i%3==0]
print(list5)

l= [8,4,7,23,45,5,9,7]
l2=[]
l.append(80)
print(l)
l.sort()
print(l)
l2 = l.copy()
print(l2)
l.sort(reverse=True)
print(l)

"""Tuple cannot be changed and if it is to be changed you should convert it into list and back to 
another tuple but you can concatenate one tuple into another""" 


tup=(1,"tori",55,6,77,80)
tup2=tup[1:4]
print(tup2)
bb= tup.count(1)
print(bb)
bb= tup.index(55)
print(bb)


cake = {"blackforest", "whiteforest", 1}
str1 = " "
if "whiteforest" in cake:
   print('nice')
   



for i in cake:
    if isinstance(i,str):
     str1 += i

    else:
       str1+=str(i)

print(str1)











