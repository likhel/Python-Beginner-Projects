class Person:
    def __init__(self,name):
        self.name = name
   

    def parent(self):
        print(f"address of {self.name} ")

class Employee(Person):
    def __init__(self,name,id,salary):
        super().__init__(name)
        self.id = id 
        self.salary = salary
    
    def parent(self):
        print("likhil")
        super().parent()

    def child(self):
        print(f"the name f the employee is {self.name} having id number{self.id} and salary of {self.salary}")
        super().parent()

P1 = Person("PRATIK")
E1 = Employee("LIKHIL",104,60000)
E1.child()
E1.parent()
