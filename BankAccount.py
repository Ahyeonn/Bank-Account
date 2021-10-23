class BankAccount:
    def __init__(self, full_name, account_number, balance=0):
        self.name = full_name
        self.acc_num = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f'\nAmount deposited: ${amount} new balance: ${self.balance}\n')
    
    def withdraw(self, amount):
        self.balance -= amount
        if amount > self.balance:
            print("Insufficient funds!!!")
            print("Overdraft fee of $10 will be applied to your account.\n")
            self.balance += 10
            print(f'Amount withdrawn: ${amount} new balance: ${self.balance}')
        else:
            print(f'Amount withdrawn: ${amount} new balance: ${self.balance}')
    
    def get_balance(self):
        print(f'Account balance: ${self.balance}\n')
        return self.balance

    def add_interest(self):
        Interest = self.balance * 0.00083
        self.balance += Interest

    def print_statement(self):
        print(self.name)
        print(f'Account No. :{self.acc_num}')
        print(f'Balance: {self.balance}\n')

mitchell_acc = BankAccount("Mitchell", "3141592")
mitchell_acc.deposit(400000)
mitchell_acc.print_statement()
mitchell_acc.add_interest()
mitchell_acc.print_statement()
mitchell_acc.withdraw(150)
mitchell_acc.print_statement()