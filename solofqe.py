import math as m

a = 1 
b = 6
c = 7

d1 = b**2 - 4*a*c
d2 = b**2 + 4*a*c

x1 = round((-b - m.sqrt(d1))/2*a)
x2 = round((-b + m.sqrt(d1))/2*a)

print("the solutions are: ",x1,x2)