from user import User
from admin import Admin
from user import Bank

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