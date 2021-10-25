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
            self.balance -= 10
            print(f'Amount withdrawn: ${amount} new balance: ${self.balance}\n')
        else:
            print(f'Amount withdrawn: ${amount} new balance: ${self.balance}\n')
    
    def get_balance(self):
        print(f'Account balance: ${self.balance}\n')
        return self.balance

    def add_interest(self):
        self.balance += self.balance * 0.00083

    def print_hidden_acc(self): #Need to have self as a parameter when it is inside the Class funciton
        new_acc = "*" * (len(self.acc_num) - 4) #append is for array, string is +=, -4 means subtracts 4 * from the len(acc.num) which is 7
        acc_numbers = list(self.acc_num)[-4:]
        # import pdb;pdb.set_trace() #for debugging. only works on global scopes
        for num in acc_numbers:
            new_acc += num
        return new_acc

    def print_statement(self):
        print(self.name)
        print(f'Account No. :{self.print_hidden_acc()}')
        self.get_balance()


