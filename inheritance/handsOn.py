# 
# WHAT IS INHERITANCE?
# --------------------

# In this one class (Child Class) to acquire the properties and methods of another
# class (Parent Class).


# Benefits:
# ---------
# 1. Code Reusability
# 2. Reduces Duplication
# 3. Easy Maintenance
# 4. Extensibility
# 5. Supports Polymorphism

# Syntax:
# --------

# class Parent:
#     pass

# class Child(Parent):
#     pass


# TYPES OF INHERITANCE

# 1. Single Inheritance
# 2. Multilevel Inheritance
# 3. Multiple Inheritance
# 4. Hierarchical Inheritance
# 5. Hybrid Inheritance

# --------------------------1. SINGLE INHERITANCE--------------------------

One child class inherits from one parent class.
    BankAccount
         |
  SavingsAccount
--------------------------------------------------
Parent Class
--------------------------------------------------

class BankAccount:

    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance")
            return
        
        self.balance -= amount
        print(f"₹{amount} withdrawn successfully.")

    def display_account(self):

        print("\n----- Account Details -----")
        print(f"Account Number : {self.account_number}")
        print(f"Holder Name    : {self.holder_name}")
        print(f"Balance        : ₹{self.balance}")


# --------------------------------------------------
# Child Class ---> SavingsAccount inherits BankAccount
# --------------------------------------------------

class SavingsAccount(BankAccount):

    def __init__(self,account_number, holder_name,balance,interest_rate):

        # Call Parent Constructor
        # SUPER()-------> # super() is used to call parent class methods and constructors.
        # Without super():
        # self.name = name
        # would need to be repeated in every child class.
        super().__init__(account_number,holder_name,balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = (self.balance *self.interest_rate / 100)
        self.balance += interest
        print( f"Interest Added: ₹{interest:.2f}")

# --------------------------------------------------
# Create Child Object
# --------------------------------------------------

account = SavingsAccount(account_number="SB1001",holder_name="Harsh Gupta",balance=50000,interest_rate=5)
# Inherited Methods
account.display_account()
account.deposit(10000)
account.withdraw(5000)

# Child Specific Method

account.add_interest()
account.display_account()


# ----------------------- 2. MULTILEVEL INHERITANCE -----------------#

"""
-----------
Multilevel Inheritance means a class inherits
from a class that already inherited from another class.

Example:

        BankAccount
             |
      SavingsAccount
             |
   PremiumSavingsAccount

PremiumSavingsAccount gets features from:
1. BankAccount
2. SavingsAccount
"""

# --------------------------------------------------
# Level 1 
# --------------------------------------------------

class BankAccount:

    def __init__(self,account_number,holder_name,balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance")
            return
        self.balance -= amount
        print(f"₹{amount} withdrawn successfully.")

    def display_account(self):
        print("\n----- Account Details -----")
        print(f"Account Number : {self.account_number}")
        print(f"Holder Name    : {self.holder_name}")
        print(f"Balance        : ₹{self.balance}")


# --------------------------------------------------
# Level 2 (Parent)
# --------------------------------------------------
# SavingsAccount inherits BankAccount
# --------------------------------------------------

class SavingsAccount(BankAccount):

    def __init__(self,account_number,holder_name,balance,interest_rate):
        super().__init__(account_number,holder_name,balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = (self.balance *self.interest_rate / 100)
        self.balance += interest

        print(f"Interest Added: ₹{interest:.2f}")


# --------------------------------------------------
# Level 3 (Child)
# --------------------------------------------------
# PremiumSavingsAccount inherits SavingsAccount
#
# Gets:
#   deposit()
#   withdraw()
#   display_account()
#   add_interest()
#
# Adds:
#   cashback_rate
#   add_cashback()
# --------------------------------------------------

class PremiumSavingsAccount(SavingsAccount):

    def __init__(self,account_number,holder_name,balance,interest_rate,cashback_rate):
        super().__init__( account_number,holder_name,balance, interest_rate)
        self.cashback_rate = cashback_rate

    def add_cashback(self, transaction_amount):
        cashback = (transaction_amount *self.cashback_rate / 100)
        self.balance += cashback
        print(f"Cashback Added: ₹{cashback:.2f}")


# --------------------------------------------------
# Create Object
# --------------------------------------------------

account = PremiumSavingsAccount(account_number="SB1001",holder_name="Harsh Gupta",balance=50000,interest_rate=5,cashback_rate=2)

# Method from BankAccount
account.deposit(10000)
# Method from BankAccount
account.withdraw(5000)
# Method from SavingsAccount
account.add_interest()
# Method from PremiumSavingsAccount
account.add_cashback(10000)
# Method from BankAccount
account.display_account()


#----------------------- 3. MULTIPLE INHERITANCE-----------

"""
Multiple Inheritance means one child class
inherits from more than one parent class.

A child class can access attributes and methods
from all parent classes.

Example:

        InterestFeature   CashbackFeature
               \              /
                \            /
                 \          /
               PremiumAccount

PremiumAccount gets features from BOTH parents.

-----WHY USE MULTIPLE INHERITANCE?------------

Suppose a bank offers:

1. Interest Benefits
2. Cashback Benefits

Instead of rewriting code in every account type,
we can create separate classes for each feature
and combine them using Multiple Inheritance.

"""


# --------------------------------------------------
# Parent Class 1---> Handles Interest Feature
# --------------------------------------------------

class InterestFeature:
    def __init__(self, interest_rate):
        self.interest_rate = interest_rate

    def calculate_interest(self, balance):
        interest = (balance * self.interest_rate / 100)

        print( f"Interest Earned: ₹{interest:.2f}")
        return interest


# --------------------------------------------------
# Parent Class 2----------> Handles Cashback Feature
# --------------------------------------------------

class CashbackFeature:
    def __init__(self, cashback_rate):
        self.cashback_rate = cashback_rate

    def calculate_cashback(self,transaction_amount):
        cashback = (transaction_amount *self.cashback_rate / 100)

        print(f"Cashback Earned: ₹{cashback:.2f}")
        return cashback


# --------------------------------------------------
# Child Class------------>Inherits from BOTH classes
#---------------------------------------------------
class PremiumAccount(InterestFeature,CashbackFeature):

    def __init__(self,account_number,holder_name,balance,interest_rate,cashback_rate):

        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

        # Initialize Parent 1
        InterestFeature.__init__( self,interest_rate)
        # Initialize Parent 2
        CashbackFeature.__init__(self,cashback_rate)

    def display_account(self):
        print("\n----- Account Details -----")
        print(f"Account Number : " f"{self.account_number}")
        print( f"Holder Name    : " f"{self.holder_name}")
        print( f"Balance        : " f"₹{self.balance:.2f}")


# --------------------------------------------------
# Create Object
# --------------------------------------------------

account = PremiumAccount(account_number="PA1001",holder_name="Harsh Gupta", balance=100000,interest_rate=5,cashback_rate=2)
account.display_account()

# Method from InterestFeature
interest = account.calculate_interest(account.balance)

# Method from CashbackFeature
cashback = account.calculate_cashback(10000)
account.balance += interest
account.balance += cashback

print(f"\nUpdated Balance: " f"₹{account.balance:.2f}")


#------------------ 4. HIERARCHICAL INHERITANCE---------------------------

# Multiple child classes inherit from one parent class.
"""
====================================================
HIERARCHICAL INHERITANCE
====================================================

Definition:
-----------
Hierarchical Inheritance means multiple child
classes inherit from a single parent class.

                    BankAccount
                   /     |      \
                  /      |       \
                 /       |        \
    SavingsAccount  CurrentAccount  SalaryAccount

All child classes inherit common banking features
from BankAccount.

====================================================
"""


# --------------------------------------------------
# Parent Class
# --------------------------------------------------

class BankAccount:

    def __init__(self,account_number,holder_name,balance):

        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited successfully.")

    def display_account(self):

        print("\n----- Account Details -----")
        print(f"Account Number : {self.account_number}")
        print(f"Holder Name    : {self.holder_name}")
        print(f"Balance        : ₹{self.balance}")


# --------------------------------------------------
# Child Class 1
# --------------------------------------------------

class SavingsAccount(BankAccount):
    def add_interest(self):

        interest = self.balance * 0.05
        self.balance += interest
        print(f"Interest Added: ₹{interest:.2f}")

# --------------------------------------------------
# Child Class 2
# --------------------------------------------------
class CurrentAccount(BankAccount):
    def issue_cheque(self):
        print(f"Cheque issued from account" f"{self.account_number}")

# --------------------------------------------------
# Child Class 3
# --------------------------------------------------

class SalaryAccount(BankAccount):
    def credit_salary(self, salary):
        self.balance += salary
        print(f"Salary of ₹{salary} credited.")


# --------------------------------------------------
# Create Objects
# --------------------------------------------------

savings = SavingsAccount("SB1001","Harsh Gupta",50000)
current = CurrentAccount("CA2001","Rahul Sharma",100000)
salary = SalaryAccount("SA3001","Amit Verma",25000)

# --------------------------------------------------
# Savings Account
# --------------------------------------------------

print("\n===== SAVINGS ACCOUNT =====")

savings.display_account()
savings.add_interest()


# --------------------------------------------------
# Current Account
# --------------------------------------------------

print("\n===== CURRENT ACCOUNT =====")

current.display_account()
current.issue_cheque()


# --------------------------------------------------
# Salary Account
# --------------------------------------------------

print("\n===== SALARY ACCOUNT =====")

salary.display_account()
salary.credit_salary(50000)



#-------------------- 5. HYBRID INHERITANCE--------------------------------
"""
Hybrid Inheritance
------------------

            BankAccount
            /        \
           /          \
SavingsAccount   LoanAccount
           \          /
            \        /
         PremiumAccount

Combination of:
1. Hierarchical Inheritance
2. Multiple Inheritance
"""


class BankAccount:
    def deposit(self):
        print("Money Deposited")


class SavingsAccount(BankAccount):
    def add_interest(self):
        print("Interest Added")


class LoanAccount(BankAccount):
    def apply_loan(self):
        print("Loan Approved")

class PremiumAccount(SavingsAccount,LoanAccount):
    def premium_benefit(self):
        print("Premium Benefits Available")

account = PremiumAccount()
account.deposit()          # From BankAccount
account.add_interest()     # From SavingsAccount
account.apply_loan()       # From LoanAccount
account.premium_benefit()  # From PremiumAccount


#---------------- METHOD OVERRIDING---------------------------------
# Child class provides its own implementation of a method that already
# exists in the parent class.


class Employee:
    def work(self):
        print("Employee performs general tasks.")


class Developer(Employee):
    def work(self):
        print("Developer writes software.")

emp = Developer()
emp.work()

"""
Search:
Developer.work() found
Parent method ignored
"""



class Employee:
    def __init__(self, name):
        self.name = name

class Developer(Employee):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language

dev = Developer("Harsh", "Python")

print(dev.name)
print(dev.language)








