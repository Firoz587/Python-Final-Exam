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


class Admin:
    def __init__(self):
        pass

    def create_account(self, bank, name, email, address, account_type):
        new_user = User(name, email, address, account_type)
        bank.users[new_user.account_number] = new_user
        print(f"Account created. Account number: {new_user.account_number}")

    def delete_account(self, bank, account_number):
        if account_number in bank.users:
            del bank.users[account_number]
            print(f"Account {account_number} deleted.")
        else:
            print("Account does not exist.")

    def view_all_accounts(self, bank):
        if not bank.users:
            print("No accounts in the bank.")
        accounts_info = []
        for acc_number, user in bank.users.items():
            accounts_info.append(f"Account: {acc_number}, Name: {user.name}, Balance: {user.balance}")
        print( "\n".join(accounts_info))

    def check_total_balance(self, bank):
        total_balance = sum(user.balance for user in bank.users.values())
        print(f"Total bank balance: {total_balance}")

    def check_total_loan(self, bank):
        print(f"Total loan amount: {bank.total_loan_amount}")

    def toggle_loan_feature(self, bank, status):
        bank.loan_feature = status
        print("Loan feature enabled" if status else "Loan feature disabled")



bank=Bank()

def users_menu():
    name = input("Enter Your Name : ")
    email = input("Enter Your Email : ")
    address = input("Enter Your Address : ")
    account_type = input("Enter Your Account Type : ")
    users = User(name=name, email=email,address=address,account_type=account_type)
    
    while True:
        print(f"Welcome {users.name}!!")
        print("1 -> Deposit")
        print("2 -> Withdraw")
        print("3 -> Check Balance")
        print("4 -> Transaction History")
        print("5 -> Take loan")
        print("6 -> Transfer")
        print("7. Exit")
        
        choice = int(input("Enter Your Choice : "))
        if choice == 1:
            users.deposit(int(input("Enter Amount : ")))
        elif choice == 2:
           users.withdraw(int(input("Enter Amount : ")))
        elif choice == 3:
            users.check_balance()
        elif choice == 4:
            users.transaction_history()
        elif choice == 5:
            users.take_loan(bank,int(input("Enter Amount :")))
        elif choice == 6:
            users.transfer(bank,int(input("Enter Account Number : ")),int(input("Enter Amount : ")))
        elif choice == 7:
            break
        else:
            print("Invalid Input")


def admin_menu():
    
    while True:
        print(f"Welcome admin Panel!!")
        print("1. Create Account")
        print("2. Delete Account")
        print("3. View All Accounts")
        print("4. Check Total Balance")
        print("5. Check Total Loan")
        print("6. Toggle Loan Feature")
        print("7. Exit")
        admin = Admin()
        choice = int(input("Enter Your Choice : "))
        if choice == 1:
            name = input("Enter Your Name : ")
            email = input("Enter Your Email : ")
            address = input("Enter Your Address : ")
            account_type = input("Enter Your Account Type : ")
            admin.create_account(bank,name,email,address,account_type)
        elif choice == 2:
            admin.delete_account(bank,int(input("Enter Account Number :")))
        elif choice == 3:
            admin.view_all_accounts(bank)
        elif choice == 4:
            admin.check_total_balance(bank)
        elif choice == 5:
            admin.check_total_loan(bank)
        elif choice == 6:
            admin.toggle_loan_feature(bank,True)
        elif choice == 7:
            break
        else:
            print("Invalid Input")

while True:
    print("Welcome!!")
    print("1. Users")
    print("2. Admin")
    print("3. Exit")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        users_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        break
    else:
        print("Invalid Input!!")