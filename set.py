sets={1,4,1,3,78,'harry'}
print(sets)
for set in sets:
    print(set)
    

students={"Likhil","Pratik","dennis","mahan","roshan"}
students2={"ramesh","prakash","kalpana","Pratik","Likhil"}
print(students.union(students2))
print(students.intersection(students2))
print(students.symmetric_difference(students2))
print(students.difference(students2))
print(students)
print(students2.isdisjoint(students))
print(students2.issubset(students)) 
'''if set A contains set B then A is superset of B and B is called subset of A'''
print(students.issuperset(students2))
students.add("harry")
print(students)
students2.remove("ramesh")
print(students2)
print(students2.discard('akon'))
 #remove and discard is almost same(delete elements from set), the only difference is that
 #remove gives error if the element to be deleted is not present but discard does not throw 
 #error
poped_item=students.pop()
print(poped_item)
del students2
students.clear()
print(students)

marks = {}