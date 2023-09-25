# Define the User class
class User():
    count = 0  # Initialize a class attribute for user count
    
    # Constructor to initialize user attributes
    def __init__(self, name, gender, salary):
        self.name = name
        self.gender = gender
        self.salary = salary
        User.count = User.count + 1  # Increment user count for each new user
        self.account = User.count  # Assign an account number
    
    # Method to display user details
    def showdetails(self):
        print(f"Name: {self.name}\nGender: {self.gender}\nSalary: {self.salary}")
        print("Account No:", self.account)

# Define the Bank class
class Bank():
    __balance = 0  # Initialize a private class attribute for bank balance
    __bankname = "DNS Bank".center(30)  # Initialize a private class attribute for bank name
    __usercount = 0  # Initialize a private class attribute for user count
    
    # Constructor to initialize bank account attributes
    def __init__(self, name, gender, salary, pin):
        self.name = name
        self.gender = gender
        self.salary = salary
        self.__pin = pin  # Private PIN attribute
        Bank.__usercount += 1  # Increment user count for each new bank account
        self.account = f"bnkaccno000{Bank.__usercount}"  # Assign an account number
    
    # Method to deposit money
    def deposit(self, amount):
        self.__balance = self.__balance + amount
        print("Amount Deposited Successfully")
        print("Your Current Balance is:", self.__balance)
    
    # Method to withdraw money
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient Balance")
            print("Your Current Balance is:", self.__balance)
        elif amount >= 100 and amount <= self.__balance:
            self.__balance = self.__balance - amount
            print("Thank You For Visiting")
            print("Your Current Bank Amount is:", self.__balance)
        elif amount < 100:
            print("You Cannot Withdraw Less Than 100")
            print("Your Current Balance is:", self.__balance)
    
    # Method to view account balance
    def viewbalance(self):
        print(f"Name: {self.name}\nGender: {self.gender}\nSalary: {self.salary}\nCurrent Balance: {self.__balance}")
    
    # Method to transfer money to another account
    def transfer(self, amt, user):
        if amt > self.__balance:
            print("Insufficient Balance")
            print("Your Current Balance is:", self.__balance)
        elif amt >= 1 and amt <= self.__balance:
            user.deposit(amt)  # Deposit amount into recipient's account
            self.__balance = self.__balance - amt  # Subtract the transferred amount
            print("Amount Transfer Successfully")
            print("Current Balance:", self.__balance)
        elif amt < 1:
            print("You Cannot Transfer amount less than 1")
            print("Current Balance:", self.__balance)
    
    # Method to get the username
    def getusername(self):
        return self.name
    
    # Method to get the PIN
    def getpin(self):
        return self.__pin
    
    # Method to return login data
    def logindata(self):
        return [self.name, self.__pin]
    
    # Method to provide a string representation of the object
    def __str__(self):
        return f"{self.name} {self.__pin}"

# Create an empty dictionary to store user objects
users = {}

# Main program loop
while True:
    print("1. Create Account\n2. Login\n3. Exit")
    choice = input("Enter your Selection: ")

    if choice == "1":
        # Create a new bank account and store it in the users dictionary
        name = input("Enter your Name: ")
        gender = input("Enter your Gender: ")
        salary = int(input("Enter your Salary: "))
        pin = input("Set your Password (PIN): ")
        users[name] = Bank(name, gender, salary, pin)

    elif choice == "2":
        # Login to an existing account
        name = input("Enter your Name: ")
        pin = input("Enter your Password (PIN): ")

        obj = users.get(name, 0)

        if obj == 0:
            print("No Match Found")
        data = obj.logindata()
        if [name, pin] in [data]:
            print("Access Granted")
            while True:
                print("1. Deposit\n2. Withdraw\n3. View Balance\n4. Transfer\n5. Logout")
                action = input("Choose an Action: ")
                if action == "1":
                    amount = int(input("Enter the deposit amount: "))
                    obj.deposit(amount)
                elif action == "2":
                    amount = int(input("Enter the withdraw amount: "))
                    obj.withdraw(amount)
                elif action == "3":
                    obj.viewbalance()
                elif action == "4":
                    accountant_name = input("Enter the Account User Name: ")
                    account = users.get(accountant_name, 0)
                    if account == 0:
                        print("Person Not Found")
                    else:
                        amount = int(input("Enter the transfer amount: "))
                        obj.transfer(amount, account)
                elif action == "5":
                    print("Logging Out")
                    break
                else:
                    print("Invalid Operation, Try again")
            else:
                print("Access Denied")
        else:
            print("Access Denied")

    elif choice == "3":
        print("Exit")
        break
