#!/usr/bin/env python3

# Define the Checkbook class to manage basic account operations
class Checkbook:
    def __init__(self):
        # Initialize the checkbook with a balance of 0.0
        self.balance = 0.0

    def deposit(self, amount):
        # Add the deposit amount to the balance
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        # Withdraw amount if sufficient funds are available
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        # Display the current balance
        print("Current Balance: ${:.2f}".format(self.balance))

# Main program loop
def main():
    cb = Checkbook()  # Create an instance of Checkbook

    # Loop to interact with the user until they choose to exit
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")

        if action.lower() == 'exit':
            break  # Exit the program

        elif action.lower() == 'deposit':
            try:
                # Ask user for deposit amount and convert to float
                amount = float(input("Enter the amount to deposit: $"))
                if amount < 0:
                    print("Please enter a positive amount.")
                    continue
                cb.deposit(amount)  # Perform deposit
            except ValueError:
                # Handle non-numeric input
                print("Invalid input. Please enter a numeric value.")

        elif action.lower() == 'withdraw':
            try:
                # Ask user for withdrawal amount and convert to float
                amount = float(input("Enter the amount to withdraw: $"))
                if amount < 0:
                    print("Please enter a positive amount.")
                    continue
                cb.withdraw(amount)  # Perform withdrawal
            except ValueError:
                # Handle non-numeric input
                print("Invalid input. Please enter a numeric value.")

        elif action.lower() == 'balance':
            # Show the current balance
            cb.get_balance()
        else:
            # Handle unrecognized commands
            print("Invalid command. Please try again.")

# Entry point of the program
if __name__ == "__main__":
    main()

