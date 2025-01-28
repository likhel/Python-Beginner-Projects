'''pi=3.14
circle = lambda n: int(pi*n**2)
sphere = lambda x,h: int(pi*x*h)

print(circle(2))

def average(c,s):
    return (c+s)//2

print(average(circle(2),sphere(4,2)))

cube = lambda y : y**3

def mid(fx,value):
    print(4+fx(value))

mid(lambda y : y**3,2)
mid(cube,2)'''

a="6"
b="6"
print(a is b) #compares exact position of a and b 
print(a == b) #compares value of a and b


a = c = "run" #immutable constant value same data and data type
b = "run"     
print(a is b)
print(c == b)

nums = [1,3,4,5] #mutable so false even if the value and data types are same
nums2 = [1,3,4,5]
print(nums is nums2)
print(nums == nums2)

g = (2,3) #immutable
d = (2,3)
i = (2,3)
print(g is d)
print(g == d)
print(g == i)
print(g is i)
 
e = None
f = None
print(e is f)
print(e == f)
print(e is None)








