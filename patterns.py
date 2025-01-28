rows = int(input("Enter a number of rows:"))
column = int(input("Enter a number of columns:"))
symbol = input("Enter a symbol:")

for i in range(rows):
    for j in range(column):
        print(symbol,end=" ")
    print()
    
