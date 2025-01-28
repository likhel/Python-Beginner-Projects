'''marks = ["30","68","87","88","53"]
students = ["Hari","Sam","Putali","maya","ram"]
std_marks = dict(zip(students,marks))

for key,value in std_marks.items():
    print(key+" : "+value)'''

fahrenheit = float(input("Enter temperature in fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print('%.2f Fahrenheit is: %0.2f Celsius' %(fahrenheit, celsius))
