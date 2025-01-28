'''x = open('myfile.txt', 'r')
text= x.read()
print(text)
x.close()

y=open('myfile2.txt','w')
y.write("hey i was here")
y.close()

z=open('myfile.txt','a')
z.write("was up guys")
z.close()

b= open('myfile2.txt', 'r') 
fun= b.read()
print(fun)
b.close()

with open('myfile2.txt','w') as c:
 c.write("visa ayo")
 

with open('myfile.txt','r') as d:
 while True:
  line=d.readline()
  print(line)
  if not line:
   print(line)
   break
   
with open('myfile.txt','w') as j:
 j.write(line)
  
m=open('marks.txt','r')
i=0
while True:
 i=i+1
 net=m.readline()
 if not net:
  break
 m1=int(net.split(",")[0])
 m2=int(net.split(",")[1])
 m3=int(net.split(",")[2])
 print(f"Marks of student{i} in MATHS : {m1}")
 print(f"Marks of student{i} in SCIENCE : {m2}")
 print(f"Marks of student{i} in ENGLISH : {m3}")
 print(net)

 with open('myfile02,txt','w') as wrt:
  list=["line1","line2","line3","line4"]
  string = "   lalalla lalalala"
  wrt.writelines(list)
  wrt.write(string)
  wrt.close()'''


with open ('myfile02.txt','r') as g :
    print(g.tell())
    g.seek(5)
    g.tell()
    print(g.tell())
    data=g.read(5)
    print(data)

with open ('go.txt', 'w') as y:
    y.write("tori maila")
    y.truncate(6)

with open("FirstFile.txt","w") as d:
    d.write("Namaste,sir!")
    print(d.tell())
    
with open("FirstFile.txt","r") as d:
   
    print(d.seek(1))
    a = d.read()
    print(a)
    
with open("FirstFile.txt","a") as d:
    d.write("\n""Khaja khanu vo?")
    print(d.tell())

with open("FirstFile.txt","w") as d:
    list1 = ['Hola',"\n"'Te Amo',"\n"'Ni Hao']
    string1 = "\n"'Halleluyah'
    d.writelines(list1)
    d.write(string1)

with open("FirstFile.txt","w+") as d:
    d.write('Lhasso Fyafulla')
    d.seek(0)
    print(d.read())




