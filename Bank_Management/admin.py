from user import User
from user import Bank

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

