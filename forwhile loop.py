sign="Dont stop here"
for i in sign:
    print(i)
subjects=["math","science","Social"] 
for subject in subjects:
    print(subject)   
    for i in subject:
       print(i)

for num in range(5):
    print(num)

for num in range(7):
    print(num+4)
for num in range(2,8):
    print(num)

for num in range(2,12,2):
    print(num)
for num in range(2,12,2):
    print(num-1)
for num in range(2,12,2):
    print(num+4)

i=0
while(i<2):
    a=int(input('enter a number:'))
    if (a==1):
     print("welcome to home page")
    elif (a==2): 
     print("welcome to admissions page")
    elif (a==3): 
      print("bye ")
    i=i+1

count=5
while(count>0):
  print(count)
  count=count-1
else:
  print("i am outside")
i=0
x=int(input("Enter a number:"))
for num in range(1,11):
    
    if(i==8):
        continue
    if(i==11):
        break
    print(x,"*",i,"=",x*i)
i=0  
while True:
      print(i)
      i=i+1
      if(i==100):
         break

fact=1    
for i in  range(1,6):
    fact=fact*i
    print(fact)

else:
    ("The work is completed")

'''here in for else loop the else sectionos executed only when the fo loop is completed'''

subjects=["Math","Science","Social","Computer"]
for subject in subjects:
    print("The {} is very easy".format(subject))
    if(subject=="Social"):
        break
else:
    print("The loop is completed")


    


     

