def greet(fx):
    def mfx(*args,**kwargs):
        print("Good morning!")
        fx(*args,**kwargs)
        print('Good night!')
    return mfx



@greet
def info():
    print("Hello World")

info()

def product(a,b):
    print("the product of two numbers is: ",a*b)

greet(product)(1,2)

