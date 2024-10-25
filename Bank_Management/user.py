from abc import ABC
import random

class Bank:
    def __init__(self):
        self.users = {}
        self.bank_balance = 0
        self.total_loan_amount = 0
        self.loan_feature = True

        
class User(ABC):
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.account_number = random.randint(100000, 999999)
        self.balance = 0
        self.transactions = []
        self.loan_count = 0

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited: {amount}")
        print(f"{amount} deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal amount exceeded.")
        self.balance -= amount
        self.transactions.append(f"Withdrew: {amount}")
        print(f"Withdrew: {amount}. New balance: {self.balance}")

    def check_balance(self):
        print(f"Available balance: {self.balance}")

    def transaction_history(self):
        if not self.transactions:
            print("No transactions yet.")
        print("\n".join(self.transactions))

    def take_loan(self, bank, amount):
        if bank.loan_feature:
            if self.loan_count >= 2:
                print("Loan limit exceeded.")
            self.loan_count += 1
            self.balance += amount
            bank.total_loan_amount += amount
            self.transactions.append(f"Loan taken: {amount}")
            print(f"Loan of {amount} granted. New balance: {self.balance}")
        print("Loan feature is disabled by the bank.")

    def transfer(self, bank, target_account, amount):
        if amount > self.balance:
            print("Insufficient funds for transfer.")
        if target_account not in bank.users:
            print("Account does not exist.")
        self.balance -= amount
        bank.users[target_account].balance += amount
        self.transactions.append(f"Transferred {amount} to {target_account}")
        bank.users[target_account].transactions.append(f"Received {amount} from {self.account_number}")
        print(f"Transferred {amount} to {target_account}. New balance: {self.balance}")
