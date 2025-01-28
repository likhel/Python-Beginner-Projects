class Club:
    name = "Real Madrid"

    def info(self):
     print(f"The name of the company is {self.name} and the name of the manager is {self.manager}")

    @classmethod
    def change(cls, newclub):  #classmethods is used to change the class attributes in normal functions 
                               #it is used to change instance variables
      cls.name = newclub

Cl = Club()
Cl.manager = "Jose"
Cl.info()
Cl.change("Chelsea")
Cl.info()
print(Cl.name)

class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    @classmethod
    def getinfo(cls,string):
        return cls(string.split("&")[0], int(string.split("&")[1]))

S1 = Student("harold", 60)
string = "Likhil&80"
print(S1.name)
print(S1.marks)
S2 = Student.getinfo(string)
print(S2.name)
print(S2.marks)

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def demo(cls,string):
        name,age = string.split(",")
        return cls(name,int(age))

per = Person.demo("YUUMY,31")
print(per.name,per.age)
