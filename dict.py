books={"name":'motivation',"id":1004,"price":500}
materials={"juice":"Fanta","biscuit":"Santa","chocolate":"zanta"}
print(books.keys())
print(books.values())
for key in books.keys():
    print(f"The value corresponding to the key {key} is {books[key]}" )

for key,value in books.items():
    print(f"The value corresponding to the key {key} is {value}" )
print(books.items())

del books["name"]
print(books)
books.update(materials)
print(books)
books.popitem()
print(books)
books.pop("price")
print(books)
books.clear()
print(books)


desert = {"fruit":"grapes","icecream":"vanilla","chocolate":"kitkat"}
print(desert["fruit"])
for key,value in desert.items():
    print(key+":"+ value)

desert.pop('fruit')
del desert['icecream']
print(desert)

'''dic = {}
n = int(input("enter the value of n:"))
for i in range(n+1):
    k = input("enter your key:")
    v = input("enter you value:")
    dic[k]=v

print(dic)'''

d1 = {"romantic":"la la land","comedy":"22 Jump Street"}
d2 = {"fiction":"lord of the rings","action thriller":"wanted"}
print(d1|d2)
print(d2)

d3 = {key:value for key,value in d1.items() if value == "22 Jump Street" }
print(d3)

d4 = {"1":1,"2":2,'3':3}
d5 = {key:value**2 for key,value in d4.items() }
print(d5)






