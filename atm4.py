class ATM:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account_name, initial_balance=0.0):
        if account_name in self.accounts:
            print("Account already exists.")
            return False
        self.accounts[account_name] = float(initial_balance)
        return True

    def remove_account(self, account_name):
        if account_name in self.accounts:
            del self.accounts[account_name]
            return True
        return False

    def get_balance(self, account_name):
        return self.accounts.get(account_name)

    def deposit_money(self, account_name, amount):
        if account_name not in self.accounts or amount <= 0:
            return False
        self.accounts[account_name] += amount
        return True

    def withdraw_money(self, account_name, amount):
        if account_name not in self.accounts:
            return False
        if amount <= 0 or amount > self.accounts[account_name]:
            return False
        self.accounts[account_name] -= amount
        return True

    def display_all_accounts(self):
        print("\nThese are all accounts currently present in the ATM:")
        for acc_id, balance in self.accounts.items():
            print(f"Account {acc_id}: ${balance:.2f}")
        print()

def main():
    atm = ATM()
    
    
    atm.add_account("Azmath", 50000.0)
    atm.add_account("rehan", 7500.0)
    atm.add_account("mehreen", 3000.0)

    
    current_account = None
    while current_account not in atm.accounts:
        current_account = input("Select your account (or enter 'new' to create one): ").strip()
        if current_account.lower() == 'new':
            name = input("Enter new account name: ").strip()
            try:
                balance = float(input("Enter initial balance: ") or "0")
                if atm.add_account(name, balance):
                    print(f"Account '{name}' created and selected.")
                    current_account = name
                else:
                    print("Account already exists. Please select another.")
                    current_account = None
            except ValueError:
                print("Invalid balance input.")
                current_account = None
        elif current_account not in atm.accounts:
            print("Account not found. Try again.")
    
    print(f"Logged in as {current_account}.")

    while True:
        print("\nCurrent Account:", current_account)
        print("1. Check balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Change account")
        print("5. View all accounts")
        print("6. Add new account")
        print("7. Remove an account")
        print("8. Exit")

        choice = input("Enter choice (1-8): ").strip()

        if choice == '1':
            balance = atm.get_balance(current_account)
            print(f"Balance for {current_account}: ${balance:.2f}")
        elif choice == '2':
            try:
                amount = float(input("Enter deposit amount: "))
                if atm.deposit_money(current_account, amount):
                    print(f"Deposited ${amount:.2f}. New balance: ${atm.get_balance(current_account):.2f}")
                else:
                    print("Invalid deposit amount.")
            except ValueError:
                print("Invalid input.")
        elif choice == '3':
            try:
                amount = float(input("Enter withdrawal amount: "))
                if atm.withdraw_money(current_account, amount):
                    print(f"Withdrew ${amount:.2f}. New balance: ${atm.get_balance(current_account):.2f}")
                else:
                    print("Invalid withdrawal or insufficient funds.")
            except ValueError:
                print("Invalid input.")
        elif choice == '4':
            new_account = input("Enter account name to switch to: ").strip()
            if new_account in atm.accounts:
                current_account = new_account
                print(f"Switched to {current_account}.")
            else:
                print("Account not found.")
        elif choice == '5':
            atm.display_all_accounts()
        elif choice == '6':
            name = input("Enter new account name: ").strip()
            try:
                balance = float(input("Enter initial balance: ") or "0")
                if atm.add_account(name, balance):
                    print(f"Account '{name}' created.")
                else:
                    print("Account already exists.")
            except ValueError:
                print("Invalid amount entered.")
        elif choice == '7':
            name = input("Enter account name to remove: ").strip()
            if atm.remove_account(name):
                print(f"Account '{name}' removed.")
                
                if name == current_account:
                    current_account = None
                    while current_account not in atm.accounts:
                        current_account = input("Select your account: ").strip()
                        if current_account not in atm.accounts:
                            print("Account not found. Try again.")
            else:
                print("Account not found.")
        elif choice == '8':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            print("noooob")

if __name__ == "__main__":
    main()
