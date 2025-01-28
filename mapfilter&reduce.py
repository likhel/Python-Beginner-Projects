l = [3, 4, 5, 6, 7, 8]

cube = lambda x: int(x)**3
newl = tuple(map(cube,l))
print(newl)

'''newl=[]
def cube(y):
  return y*y*y

for item in l:
 newl.append(cube(item))
 
print(newl)'''

l1 = [20, 35,24, 56, 70, 570, 555, 64]
def filt(n):
     return n%5 == 0

l2 = list(filter(filt,l1))
print(l2)

from functools import reduce

l3 = [1, 2, 3, 4 , 5]
def product(p,q):
     return p*q

pro = lambda x,y: x*y

l4 = reduce(pro,l3)
print(l4)
