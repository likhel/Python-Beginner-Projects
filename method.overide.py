'''class Animal():
    def run(self):
        print("you can run")

class Dog(Animal):
    def eat(self):
        print("dog can run")

D1 = Dog()
D1.eat()'''

class Person():
    def __init__(self,name):
        self.name = name

    def show(self):
        print(self.name)

class Hari(Person):
    def show1(self):
        print(f"{self.name}")

h = Hari('rAM')
h.show()

class College():
    def __init__(self,name,location,phone):
        self.name = name
        self.location = location
        self.phone = phone

class Computer(College):
    def __init__(self,name,location,phone,sem,totalsub,):
        super().__init__(name,location,phone)
        self.sem = sem
        self.totalsub = totalsub
       
    def show_details(self):
        print(f"Name = {self.name} address = {self.location} sem = {self.sem}")

Com = Computer("Acme","Sitapaila",96986969,4,42)
Com.show_details()

print(hasattr(Com,"sem"))
print(getattr(Com,"sem"))
print(setattr(Com,"sem",5))
print(delattr(Com,"totalsub"))
print(getattr(Com,"sem"))

        