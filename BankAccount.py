class BankAccount:
    def __init__(self, full_name, account_number, balance=0):
        self.name = full_name
        self.acc_num = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f'Amount deposited: ${amount} new balance: ${self.balance}')
   
ahyeon_acc = BankAccount("Ahyeon Jeon", "12345678", 30)
ahyeon_acc.deposit(50)
