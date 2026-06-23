# encapsulation_demo.py

print("=" * 60)
print("ENCAPSULATION IN PYTHON")
print("=" * 60)


# =====================================================
# 1. BASIC ENCAPSULATION
# =====================================================

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance   # private variable

    def show_balance(self):
        print(f"Balance: ₹{self.__balance}")


acc = BankAccount("Unnati", 5000)

print("\n1. BASIC ENCAPSULATION")
print("Owner:", acc.owner)
acc.show_balance()

# print(acc.__balance)  # Error


# =====================================================
# 2. GETTER METHOD
# =====================================================

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary


emp = Employee("Rahul", 60000)

print("\n2. GETTER METHOD")
print("Salary:", emp.get_salary())


# =====================================================
# 3. SETTER METHOD
# =====================================================

class Student:
    def __init__(self, name):
        self.name = name
        self.__marks = 0

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks")

    def get_marks(self):
        return self.__marks


s1 = Student("Aman")

print("\n3. SETTER METHOD")
s1.set_marks(85)
print("Marks:", s1.get_marks())

s1.set_marks(120)
print("Marks:", s1.get_marks())


# =====================================================
# 4. DEPOSIT AND WITHDRAW
# =====================================================

class Account:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance


acc = Account(10000)

print("\n4. DEPOSIT AND WITHDRAW")

acc.deposit(5000)
acc.withdraw(2000)

print("Balance:", acc.get_balance())


# =====================================================
# 5. PROPERTY DECORATOR
# =====================================================

class Product:
    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value
        else:
            print("Price must be positive")


p1 = Product(100)

print("\n5. PROPERTY DECORATOR")
print("Price:", p1.price)

p1.price = 500
print("Updated Price:", p1.price)

p1.price = -50


# =====================================================
# 6. NAME MANGLING
# =====================================================

class Demo:
    def __init__(self):
        self.__secret = "Hidden Data"


d = Demo()

print("\n6. NAME MANGLING")

# print(d.__secret)   # Error

print("Access using name mangling:")
print(d._Demo__secret)


# =====================================================
# 7. REAL WORLD EXAMPLE
# =====================================================

class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def check_password(self, entered_password):
        return entered_password == self.__password

    def change_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
            print("Password updated")
        else:
            print("Wrong old password")


u1 = User("unnati", "1234")

print("\n7. REAL WORLD EXAMPLE")

print(u1.check_password("1234"))
print(u1.check_password("abcd"))

u1.change_password("1234", "newpass")
print(u1.check_password("newpass"))


# =====================================================
# 8. PRIVATE METHODS
# =====================================================

class Database:
    def connect(self):
        self.__authenticate()
        print("Connected to database")

    def __authenticate(self):
        print("Authentication successful")


db = Database()

print("\n8. PRIVATE METHODS")
db.connect()


# =====================================================
# 9. WHY ENCAPSULATION
# =====================================================

print("\n9. BENEFITS")
print("""
1. Data hiding
2. Data protection
3. Controlled access
4. Validation before modification
5. Cleaner code
6. Better security
""")
