currentpw="PPPWWW"
str1=input('Enter the password:')
match str1:
    case 1 if str1==currentpw: 
        print("The password is correct")
           
    case _:
          print("The password is invaliD")
          
             
