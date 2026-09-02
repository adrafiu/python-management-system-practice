accounts = []

# Create account
def create_account():
    
    account_no = input("Enter Account Number: ")
    name = input("Enter Account Holder Name: ")
    
    try:
        balance = float(input("Inter Initial Balance: "))
        
        if balance < 0:
            print("Balance Cannot Be Negative.")
            return
        
    except ValueError:
        print("Enter a Valid Amount.")
        return
    account = {
        "account_no": account_no,
        "name": name,
        "balance": balance
    }
    
    accounts.append(account)
    print("Account Created Successfully.") 
    
# View Account 
def view_account():
    
    if len(accounts) == 0:
        print("No Account Available.")
        return
    
    for account in accounts:
        print(account)
    
# search account       
def search_account():

    account_no = input("Enter Account Number: ")

    for account in accounts:

        if account["account_no"] == account_no:
            print(account)
            return

    print("Account Not Found.")
  
# Deposite
def deposite():
    
    account_no = input("Enter Account Number: ")
    
    for account in accounts:
        if account["account_no"] == account_no:
            
            try:
                amount = float(input("Enter Deposite Amount: "))
                
                if amount <= 0:
                    print("Amount must be greater than 0.")
                    return
                
            except ValueError:
                print("Enter a Valid Amount.")
                return
            
            account["balance"] += amount
            
            print("Deposite Successful.")
            print(f"New Balance: {account["balance"]}")  
            
            return
    print("Account Not Found.")   
    
# Withdraw
def withdraw():
    account_no = input("Enter Account Number: ")
    
    for account in accounts:
        if account ["account_no"] == account_no:
            
            try:
                amount = float(input("Enter Withdraw Amount: "))
                
                if amount <= 0:
                    print("Amount Must Be Greater Than 0.")
                    return
                
            except ValueError:
                print("Enter a Valid Amount.")
                return
            if amount > account["balance"]:
                print("Insufficient Balance.")
                return
            
            account["balance"] -= amount
            
            print("Withdraw Successful.")
            print(f"New Balance: {account["balance"]}")
            
            return
    print("Account Not Found.")
    
# Delete Account 
def delete_account():
    
    account_no = input("Enter Account Number: ")
    
    for account in accounts:
        if account["account_no"] == account_no:
            
            accounts.remove(account)
            print("Account Deleted Successfuly.")
            
            return
    print("Account Not Found.") 
    
# Main Menu
while True:
    
    print("""
    ==Bank Management System ==
    
    1. Create Account
    2. View Accounts
    3. Search Account
    4. Deposit
    5. Withdraw
    6. Delete Account
    7. Exit
    
    """)
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        create_account()
        
    elif choice == "2":
        view_account()
        
    elif choice == "3":
        search_account()
        
    elif choice == "4":
        deposite() 
        
    elif choice == "5":
        withdraw()
        
    elif choice == "6":
        delete_account()
        
    elif choice == "7":
        break
    
    else:
        print("Invalid Choice.")                           