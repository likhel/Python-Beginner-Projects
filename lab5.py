'''class Students:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def show_info(self):
        print(f"The name of the student is {self.name}")
        print(f"The age of the student is {self.age}")
        print(f"The grade of the student is {self.grade}")

st1 = Students("hari", "20", "A")
st1.show_info() '''


'''class Square:

    def show_area(self,length):
        area = length**2
        return area
    def show_perimeter(self,length):
        perimeter = 4*length
        return perimeter
    
sq1 = Square()
l = int(input("Enter the length:"))
a = sq1.show_area(l)
b = sq1.show_perimeter(l)
print(f"Area = {a} and Perimeter = {b}")'''

class Atm:
    def __init__(self, balance):
        self.balance = balance
        self.menu()
        
        
    def menu(self):
        user_input = input("""
            Enter 1 for check balance.
            Enter 2 for withdraw
            Enter 3 to see user details
            Enter 4 to deposit money 
            Enter 5 to take a loan
                           
            """)
        if user_input == "1":
            self.check_balance()
        elif user_input == "2":
            self.balance_withdraw()
        elif user_input == "3":
            self.user_details()
        elif user_input == "4":
            self.deposit()
        elif user_input == "5":
             self.loan()
    
    def user_details(self):
        p = input('enter your name:')
        q = int(input('enter your age:'))
        r = input('Enter your address:')
        self.menu()

    def check_balance(self):
        print(f"your current balance is {self.balance}")
        self.menu()

    def balance_withdraw(self):
                
        try:
                w_balance = int(input("Enter your balance to withdraw:"))

                if w_balance <= 0:
                        print("Invalid amount. Please enter a positive number.")
                elif self.balance >= w_balance:
                    self.balance = self.balance-w_balance
                    print(f"You have withdrawn {w_balance}\n New Balance = {self.balance}")
                else:
                    print("Insufficient Funds!")
                self.menu()
        
        except ValueError:
            print("Invalid input. Please enter a number.")

        


    def deposit(self):

        try:
                dep_money = int(input("Enter the amount to deposit:"))

                if  dep_money <= 0:
                        print("Invalid amount. Please enter a positive number.")
                else:
                    self.balance += dep_money
                    print(f"{dep_money} has been granted.\n New Balance = {self.balance}")

                  
        
        except ValueError:
            print("Invalid input. Please enter a number.")

    def loan(self):
         try:
              
              loan_amount = int(input("Enter the loan amount:"))
              if loan_amount <= 0:
                   print("Enter positive integer")
              else:
                   self.balance += loan_amount
                   print(f"{loan_amount} has been granted.\n New Balance = {self.balance}")

         except ValueError:
              print("Invalid input.Please enter a number")
                   
                   
         
                

atm = Atm(7000)


