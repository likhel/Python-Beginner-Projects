farhan = int(input("Enter the temperature in farenheit:"))
cels = int(input("Enter the temperature in cels:")) 


def change_f(f):
    c = (f-32)*5/9
    print(f"the converted temperature from fareheit to celsius:{round(c,2)}")
    
     

def change_c(c):
  
    f = (9*c/5)+32
    print(f"the converted temperature from celsius to fareheit:{round(f,2)}")

change_f(farhan)
change_c(cels)