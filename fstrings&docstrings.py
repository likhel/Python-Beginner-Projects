book="its like {} my  mirror my mirror {} back at me"
word='in'
word2='staring'
print(book.format(word,word2))

page="Show {1} how to {0} for now"
w1='me'
w2='fight'
print(page.format(w2,w1))
print(f"its like {word} my mirror my mirror {word2} back at me")
price=25.5656
print(f"the price of 1 litre petrol is {price:.2f} Rs")

def cube(l):
    '''hardwork and 
    dedication'''
    print("the volume of a cube is",l**3)

cube(5)
print(cube.__doc__)
