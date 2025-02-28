# Task 1

class Animal:
    def __init__(self, name, age, sound, breed, weight):
        self.name = name
        self.age = age
        self.sound = sound
        self.breed = breed
        self.weight = weight
        self.hungry = False

    def make_sound(self):
        if self.hungry:
            return f"{self.name} is hungry and says {self.sound.upper()}!"
        return f"{self.name} says {self.sound}"

    def eat(self):
        self.hungry = False
        return f"{self.name} is eating."

    def sleep(self):
        self.hungry = True
        return f"{self.name} is sleeping."

class Cow(Animal):
    def __init__(self, name, age, breed, weight):
        super().__init__(name, age, "Moo", breed, weight)

    def produce_milk(self):
        return f"{self.name} is producing milk."

class Chicken(Animal):
    def __init__(self, name, age, breed, weight):
        super().__init__(name, age, "Cluck", breed, weight)

    def lay_egg(self):
        return f"{self.name} laid an egg."

class Sheep(Animal):
    def __init__(self, name, age, breed, weight):
        super().__init__(name, age, "Baa", breed, weight)

    def shear(self):
        return f"{self.name} is being sheared."

cow = Cow("Bessie", 5, "Holstein", 1500)
chicken = Chicken("Clucky", 2, "Leghorn", 5)
sheep = Sheep("Woolly", 3, "Merino", 120)

print(cow.make_sound())
print(cow.eat())
print(cow.sleep())
print(cow.produce_milk())

print(chicken.make_sound())
print(chicken.eat())
print(chicken.sleep())
print(chicken.lay_egg())

print(sheep.make_sound())
print(sheep.eat())
print(sheep.sleep())
print(sheep.shear())

# Task 2

import json
import os

class Account:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"Account Number: {self.account_number}, Name: {self.name}, Balance: {self.balance}"

class Bank:
    def __init__(self, file_path="accounts.txt"):
        self.accounts = {}
        self.file_path = file_path
        self.load_from_file()

    def create_account(self, name, initial_deposit):
        account_number = len(self.accounts) + 1
        account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = account
        self.save_to_file()
        print(f"Account created successfully! Account Number: {account_number}")

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(account)
        else:
            print("Account not found.")

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            if amount > 0:
                account.balance += amount
                self.save_to_file()
                print(f"Deposited {amount} successfully! New Balance: {account.balance}")
            else:
                print("Invalid deposit amount.")
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            if 0 < amount <= account.balance:
                account.balance -= amount
                self.save_to_file()
                print(f"Withdrew {amount} successfully! New Balance: {account.balance}")
            else:
                print("Invalid withdrawal amount.")
        else:
            print("Account not found.")

    def save_to_file(self):
        try:
            with open(self.file_path, 'w') as file:
                json.dump({acc_num: acc.__dict__ for acc_num, acc in self.accounts.items()}, file)
        except Exception as e:
            print(f"An error occurred while saving to file: {e}")

    def load_from_file(self):
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r') as file:
                    accounts_data = json.load(file)
                    for acc_num, acc_data in accounts_data.items():
                        self.accounts[int(acc_num)] = Account(**acc_data)
            except Exception as e:
                print(f"An error occurred while loading from file: {e}")

def get_valid_input(prompt, input_type):
    while True:
        try:
            return input_type(input(prompt))
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}.")


bank = Bank()

while True:
    print("\nMenu Options:")
    print("1. Create new account")
    print("2. View account details")
    print("3. Deposit money")
    print("4. Withdraw money")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        name = input("Enter your name: ")
        initial_deposit = get_valid_input("Enter initial deposit: ", float)
        bank.create_account(name, initial_deposit)
    elif choice == '2':
        account_number = get_valid_input("Enter account number: ", int)
        bank.view_account(account_number)
    elif choice == '3':
        account_number = get_valid_input("Enter account number: ", int)
        amount = get_valid_input("Enter deposit amount: ", float)
        bank.deposit(account_number, amount)
    elif choice == '4':
        account_number = get_valid_input("Enter account number: ", int)
        amount = get_valid_input("Enter withdrawal amount: ", float)
        bank.withdraw(account_number, amount)
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")