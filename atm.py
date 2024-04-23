class ATM:
    def __init__(self):
        self.card_number = input("Enter your card number: ")
        self.pin_number = input("Enter your PIN: ")
        self.balance = 1000  

    def cash_withdrawal(self):
        amount = float(input("Enter withdrawal amount: $"))
        if 0 < amount <= self.balance:
            print("Cash withdrawal initiated...")
            print(f"Withdrawn amount: ${amount}")
            self.balance -= amount
            print(f"Remaining balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def balance_enquiry(self):
        print("Balance enquiry initiated...")
        print(f"Your current balance is ${self.balance}")



if __name__ == "__main__":
    user_atm = ATM()

    user_atm.cash_withdrawal()
    user_atm.balance_enquiry()
   
