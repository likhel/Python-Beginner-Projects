class Atm:
    def __init__(self, balance):
        self.balance = balance
        self.users = {}  # Dictionary to store user credentials
        self.current_user = None
        self.transaction_history = []
        self.start()

    def start(self):
        while True:
            choice = input("""
                Enter 1 to login.
                Enter 2 to register.
                Enter 3 to exit.
                
                Your choice: """)
            if choice == "1":
                self.user_login()
            elif choice == "2":
                self.user_registration()
            elif choice == "3":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def user_registration(self):
        name = input("Enter your name to register: ")
        if name in self.users:
            print("This name is already registered. Please choose a different name.")
            return
        password = input("Enter your password: ")
        self.users[name] = {'password': password, 'balance': self.balance, 'transaction_history': []}
        print(f"User {name} registered successfully!")

    def user_login(self):
        name = input("Enter your name to login: ")
        if name not in self.users:
            print("No such user found. Please register first.")
            return
        password = input("Enter your password: ")
        if self.users[name]['password'] == password:
            self.current_user = name
            print(f"User {name} logged in successfully!")
            self.menu()
        else:
            print("Incorrect password. Please try again.")

    def menu(self):
        while True:
            user_input = input("""
                Enter 1 to check balance.
                Enter 2 to withdraw.
                Enter 3 to see user details.
                Enter 4 to deposit money.
                Enter 5 to take a loan.
                Enter 6 to view transaction history.
                Enter 7 to logout.
                
                Your choice: """)
            if user_input == "1":
                self.check_balance()
            elif user_input == "2":
                self.balance_withdraw()
            elif user_input == "3":
                self.user_details()
            elif user_input == "4":
                self.deposit()
            elif user_input == "5":
                self.take_loan()
            elif user_input == "6":
                self.view_transaction_history()
            elif user_input == "7":
                print(f"User {self.current_user} logged out.")
                self.current_user = None
                break
            else:
                print("Invalid choice. Please try again.")

    def check_balance(self):
        balance = self.users[self.current_user]['balance']
        print(f"Your current balance is {balance}")
        self.users[self.current_user]['transaction_history'].append(f"Checked balance: {balance}")

    def balance_withdraw(self):
        try:
            w_balance = int(input("Enter the amount to withdraw: "))
            if w_balance <= 0:
                print("Invalid amount. Please enter a positive number.")
            elif self.users[self.current_user]['balance'] >= w_balance:
                self.users[self.current_user]['balance'] -= w_balance
                print(f"You have withdrawn {w_balance}. New balance: {self.users[self.current_user]['balance']}")
                self.users[self.current_user]['transaction_history'].append(f"Withdrew {w_balance}. New balance: {self.users[self.current_user]['balance']}")
            else:
                print("Insufficient funds!")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def deposit(self):
        try:
            dep_money = int(input("Enter the amount to deposit: "))
            if dep_money <= 0:
                print("Invalid amount. Please enter a positive number.")
            else:
                self.users[self.current_user]['balance'] += dep_money
                print(f"You have deposited {dep_money}. New balance: {self.users[self.current_user]['balance']}")
                self.users[self.current_user]['transaction_history'].append(f"Deposited {dep_money}. New balance: {self.users[self.current_user]['balance']}")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def user_details(self):
        print(f"Name: {self.current_user}")
        print(f"Balance: {self.users[self.current_user]['balance']}")
        self.users[self.current_user]['transaction_history'].append(f"Viewed user details for {self.current_user}")

    def take_loan(self):
        try:
            loan_amount = int(input("Enter the loan amount: "))
            if loan_amount <= 0:
                print("Invalid amount. Please enter a positive number.")
            else:
                self.users[self.current_user]['balance'] += loan_amount
                print(f"Loan of {loan_amount} granted. New balance: {self.users[self.current_user]['balance']}")
                self.users[self.current_user]['transaction_history'].append(f"Loan of {loan_amount} granted. New balance: {self.users[self.current_user]['balance']}")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def view_transaction_history(self):
        if self.users[self.current_user]['transaction_history']:
            print("Transaction History:")
            for transaction in self.users[self.current_user]['transaction_history']:
                print(transaction)
        else:
            print("No transactions yet.")

atm = Atm(7000)
