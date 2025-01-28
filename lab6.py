'''class Vechile():
    def drive(self):
        pass

class Car(Vechile):

    def drive(self):
        print("You can drive car")

class Bicycle(Vechile):

    def drive(self):
        print("You can drive bicycle")

B1 = Bicycle()
B1.drive()

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
class Student(Person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade = grade
    
    def show_details(self):
        print(f"name = {self.name} age = {self.age} grade = {self.grade}")

class Teacher(Person):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject = subject
    
    def show_details(self):
        print(f"name = {self.name} age = {self.age} grade = {self.subject}")

St = Student('LIKHIL',22,"A")
Tc = Teacher('Ramesh',30,"Science")
St.show_details()
Tc.show_details()

def div(x,y):
    try:
      
       x/y
    except ZeroDivisionError as ze:
      print(ze)

    


a = int(input("Enter an integer:"))
b = int(input("Enter another integer:"))
div(a,b)'''

def check_age(x):
  try:  
    if x>16:
        print('You can vote')
    elif x<16:
        raise Exception("you should be over 16 to vote")
  except ValueError as ve:
     
     print(ve)
    
    
    
    
age = int(input("Enter you age:"))
check_age(age)


