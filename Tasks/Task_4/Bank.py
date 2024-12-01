class Bank:
    def __init__(self, balance):
        self.balance = balance
        
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
        else:
            self.balance += amount
            print(f'Deposited {amount}. New balance: {self.balance}')

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print('Insufficient funds.')
        else:
            self.balance -= amount
            print(f'Withdrew {amount}. New balance: {self.balance}')

    def check_balance(self):
        print(f'Current balance: {self.balance}')

def get_valid_input(prompt):
    while True:
        try:
            return float(input(prompt))  
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == '__main__':
    balance = get_valid_input('Enter your initial balance: ') 
    b = Bank(balance)
    
    while True:
        print("\nChoose an operation:")
        print("1: Deposit")
        print("2: Withdraw")
        print("3: Check Balance")
        print("4: Exit")
        
        choice = input("Enter your choice (1-2-3-4): ")

        if choice == '1':
            amount = get_valid_input("Enter amount to deposit: ")
            b.deposit(amount)
        elif choice == '2':
            amount = get_valid_input("Enter amount to withdraw: ")
            b.withdraw(amount)
        elif choice == '3':
            b.check_balance()
        elif choice == '4':
            print("Exiting... Thank you for using our service!")
            break 
        else:
            print("Invalid choice! Please select a valid option.")
