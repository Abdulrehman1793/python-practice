#case 2:- bank account management

class BankAccount:
    def __init__(self, account_number, initial_balance=0):
       self.account_no = account_number
       self.current_balance = initial_balance
       print(f'Account {account_number} has balance {self.current_balance}')

    def get_balance(self):
        return self.current_balance
    
    def deposit(self, amount = 0):
        if amount <= 0:
            print("Amount should be greater than zero")
            return
        self.current_balance = self.current_balance + amount
        print(f'After Deposit {amount}, You current balance is {self.current_balance}')

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount should be greater than zero")
            return
        
        if self.current_balance > amount:
            self.current_balance = self.current_balance - amount
        else:      
            print("Insufficient funds" )
        print(f'After Withdrawal {amount}, You current balance is {self.current_balance}')

#example 1
khalid = BankAccount("ABCK2158", 10)
khalid.deposit(5)
khalid.withdraw(5)
    
