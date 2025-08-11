class ATM:
    def __init__(self):
        self.balance = 0
    
    
    def check_balance(self):
        return f"Your current balance is: ${self.balance:.2f}"
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Successfully deposited ${amount:.2f}. {self.check_balance()}"
        else:
            return "Invalid deposit amount. Please enter a positive value."
    
    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                return f"Successfully withdrew ${amount:.2f}. {self.check_balance()}"
            else:
                return "Insufficient funds. Withdrawal amount exceeds balance."
        else:
            return "Invalid withdrawal amount. Please enter a positive value."
    def delete_account(self , amount):
        if amount > 0:
            self.balance -= self.balance
            return f"successfully deleted your account"
        else:
            print ("your account balance is 0")

def run_atm():
    atm = ATM()
    name = input("please enter your name :")
    
    while True:
        print("\nWelcome to the ATM" , name)
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. delete account")
        print("5.Exit")
        
        choice = input("Please select an option (1-5): ")
        
        if choice == '1':
            print(atm.check_balance())
        elif choice == '2':
            try:
                amount = float(input("Enter deposit amount: $"))
                print(atm.deposit(amount))
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif choice == '3':
            try:
                amount = float(input("Enter withdrawal amount: $"))
                print(atm.withdraw(amount))
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif choice == "4":
            print ("your account has been reset to :" , atm.delete_account(amount))
        elif choice == '5':
            print("Thank you for using our ATM. Goodbye!" , name)
        break
    else:
        print("invalid number ,select from 1-5" )
        


if __name__ == "__main__":
    run_atm()
