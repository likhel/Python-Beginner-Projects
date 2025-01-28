'''class Employee :
    
    name = "john"
    salary = 40000
    id = 1005
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def info(self):
        print(f"{self.name} earns {self.salary} a month")

#a = Employee("likhil", "50000")

a = Employee("likhil", "50000")
a.name = input("enter your name:")
a.salary = input("enter your salary:")

a.info()'''

class cal:

    def __init__(self,name,age):
      self.n = name
      self.a = age
    def __str__(self) :
       return f"{self.n}{self.a}"

obj = cal("rocky",10)
print(obj)


