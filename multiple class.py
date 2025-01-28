'''class Person:
    def get_info(self, name, age):
        print("name = ", name)
        print("age = ", age)
       
class School:
    def set_info(self, scname, scaddress):
        print("schoolname = ", scname)
        print("schooladdress = ", scaddress)

class Employee(Person, School):
    pass

obj1 = Employee()
obj1.get_info("Dennis",20)
obj1.set_info("Lri","Kalanki, Kathmandu")'''

#Multilevel Inheritance

'''class Person:
    def get_person_info(self, name, age):
        print("name = ", name)
        print("age = ", age)
       
class School(Person):
    def get_school_info(self, scname, scaddress):
        print("schoolname = ", scname)
        print("schooladdress = ", scaddress)

class Employee(School):
    def get_employee_info(self, name, salary):
        print("Employee name:", name)
        print("The salary is:", salary)

class Department(Employee):
    pass

obj_dept= Department()


obj_dept.get_person_info("Dennis",20)
obj_dept.get_school_info("Lri","Kalanki, Kathmandu")
obj_dept.get_employee_info("Likhil", "$5000")'''

#Hierarchical Inheritance

class Car:
    def get_car(self, name):
        print("The car is :", name)
class Mercedes(Car):
    def get_mercedes(self):
        pass
class Lamborghini(Car):
    def get_lambo(self):
        pass

obj_m = Mercedes()
obj_l = Lamborghini()

obj_m.get_car("Mercedes")
obj_l.get_car("Lamborghini")



