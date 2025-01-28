import math

'''def cal(r = 3,R=2):
    print(f"the area of the first circle is:{round(math.pi*r**2)}")
    print(f"the perimeter of the first circle is:{round(math.pi*2*r)}")
    print(f"the area of the second circle is:{round(math.pi*R**2)}")
    print(f"the perimeter of the second circle is:{round(math.pi*2*R)}")'''

def ok(r,R):

    print(f"the area of the first circle is:{round(math.pi*r**2)}")
    print(f"the perimeter of the first circle is:{round(math.pi*2*r)}")
    print(f"the area of the second circle is:{round(math.pi*R**2)}")
    print(f"the perimeter of the second circle is:{round(math.pi*2*R)}")

    
r1 = int(input("enter the radius for first circle:"))
r2 = int(input("enter the radius for second circle:"))
ok(r = r1, R = r2)