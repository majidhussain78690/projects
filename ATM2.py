import random
import string
class ATM:
    def __init__(self):
        self.accounts = {}
        self.generate_default_accounts()
        
    def generate_default_accounts(self):
        """Generate 5 default accounts with random balances between 100 and 5000"""
        for i in range(1, 6):
            account_id = f"Default{i}"
            balance = round(random.uniform(100, 1000), 2)
            self.accounts[account_id] = balance
    
    def generate_account_id(self):
        """Generate a random 6-digit account ID"""
        return ''.join(random.choices(string.digits, k=6))
    
    def add_account(self, initial_balance=0.0):
        """Add a new account with given initial balance"""
        account_id = self.generate_account_id()
        while account_id in self.accounts:
            account_id = self.generate_account_id()
            
        self.accounts[account_id] = initial_balance
        return account_id
    
    def remove_account(self, account_id):
        """Remove an account if it exists"""
        if account_id in self.accounts:
            del self.accounts[account_id]
            return True
        return False
    
    def get_balance(self, account_id):
        """Check account balance"""
        return self.accounts.get(account_id, None)
    
    def deposit(self, account_id, amount):
        """Deposit money into account"""
        if account_id not in self.accounts:
            return False
        
        if amount <= 0:
            return False
            
        self.accounts[account_id] += amount
        return True
    
    def withdraw(self, account_id, amount):
        """Withdraw money from account"""
        if account_id not in self.accounts:
            return False
            
        if amount <= 0 or amount > self.accounts[account_id]:
            return False
            
        self.accounts[account_id] -= amount
        return True
    
    def display_accounts(self):
        """Display all accounts and their balances"""
        print("\nCurrent Accounts:")
        for acc_id, balance in self.accounts.items():
            print(f"Account {acc_id}: ${balance:.2f}")
        print()

def main():
    atm = ATM()
    
    while True:
        print("\n1. View all accounts")
        print("2. Check balance")
        print("3. Deposit money")
        print("4. Withdraw money")
        print("5. Add new account")
        print("6. Remove account")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == "1":
            atm.display_accounts()
            
        elif choice == "2":
            account_id = input("Enter account ID: ")
            balance = atm.get_balance(account_id)
            if balance is not None:
                print(f"Account {account_id} balance: ${balance:.2f}")
            else:
                print("Account not found!")
                
        elif choice == "3":
            account_id = input("Enter account ID: ")
            try:
                amount = float(input("Enter deposit amount: "))
                if atm.deposit(account_id, amount):
                    print(f"Deposited ${amount:.2f} to account {account_id}")
                    print(f"New balance: ${atm.get_balance(account_id):.2f}")
                else:
                    print("Deposit failed. Invalid account or amount.")
            except ValueError:
                print("Invalid amount entered.")
                
        elif choice == "4":
            account_id = input("Enter account ID: ")
            try:
                amount = float(input("Enter withdrawal amount: "))
                if atm.withdraw(account_id, amount):
                    print(f"Withdrew ${amount:.2f} from account {account_id}")
                    print(f"New balance: ${atm.get_balance(account_id):.2f}")
                else:
                    print("Withdrawal failed. Invalid account, amount, or insufficient funds.")
            except ValueError:
                print("Invalid amount entered.")
                
        elif choice == "5":
            try:
                initial_balance = float(input("Enter initial balance (default 0): ") or 0)
                new_account = atm.add_account(initial_balance)
                print(f"New account created: {new_account} with balance ${initial_balance:.2f}")
            except ValueError:
                print("Invalid amount entered.")
                
        elif choice == "6":
            account_id = input("Enter account ID to remove: ")
            if atm.remove_account(account_id):
                print(f"Account {account_id} removed successfully.")
            else:
                print("Account not found!")
                
        elif choice == "7":
            print("Thank you for using the ATM. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()