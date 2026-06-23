# polymorphism_demo.py

print("=" * 70)
print("POLYMORPHISM IN PYTHON")
print("=" * 70)

"""
Polymorphism means:
Same method/operator/function name, but different behavior depending on object.

Simple meaning:
One name, many forms.
"""


# ======================================================
# 1. BASIC POLYMORPHISM WITH SAME METHOD NAME
# ======================================================

print("\n1. BASIC POLYMORPHISM")
print("-" * 70)


class Dog:
    def sound(self):
        print("Dog says: Bark")


class Cat:
    def sound(self):
        print("Cat says: Meow")


class Cow:
    def sound(self):
        print("Cow says: Moo")


animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.sound()


# ======================================================
# 2. POLYMORPHISM USING FUNCTION
# ======================================================

print("\n2. POLYMORPHISM USING FUNCTION")
print("-" * 70)


class Car:
    def start(self):
        print("Car starts with key/button")


class Bike:
    def start(self):
        print("Bike starts with self-start/kick")


class Laptop:
    def start(self):
        print("Laptop starts with power button")


def start_anything(obj):
    obj.start()


start_anything(Car())
start_anything(Bike())
start_anything(Laptop())


# ======================================================
# 3. DUCK TYPING
# ======================================================

print("\n3. DUCK TYPING")
print("-" * 70)

"""
Duck typing means Python does not care about the exact class.
It only cares whether the object has the required method or not.
"""


class Duck:
    def walk(self):
        print("Duck is walking")

    def sound(self):
        print("Duck says: Quack")


class Person:
    def walk(self):
        print("Person is walking")

    def sound(self):
        print("Person imitates: Quack")


def test_duck_behavior(obj):
    obj.walk()
    obj.sound()


test_duck_behavior(Duck())
test_duck_behavior(Person())


# ======================================================
# 4. METHOD OVERRIDING
# ======================================================

print("\n4. METHOD OVERRIDING")
print("-" * 70)

"""
Method overriding happens when child class has the same method
as parent class, but with different implementation.
"""


class Animal:
    def speak(self):
        print("Animal makes a sound")


class Lion(Animal):
    def speak(self):
        print("Lion roars")


class Snake(Animal):
    def speak(self):
        print("Snake hisses")


a1 = Animal()
a2 = Lion()
a3 = Snake()

a1.speak()
a2.speak()
a3.speak()


# ======================================================
# 5. POLYMORPHISM WITH INHERITANCE
# ======================================================

print("\n5. POLYMORPHISM WITH INHERITANCE")
print("-" * 70)


class Payment:
    def pay(self, amount):
        print(f"Paying ₹{amount}")


class UpiPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class CardPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Card")


class CashPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Cash")


payments = [UpiPayment(), CardPayment(), CashPayment()]

for payment in payments:
    payment.pay(500)


# ======================================================
# 6. OPERATOR POLYMORPHISM
# ======================================================

print("\n6. OPERATOR POLYMORPHISM")
print("-" * 70)

print("5 + 3 =", 5 + 3)
print("'Hello ' + 'Python' =", "Hello " + "Python")
print("[1, 2] + [3, 4] =", [1, 2] + [3, 4])

"""
Same + operator:
numbers -> addition
strings -> concatenation
lists -> merging
"""


# ======================================================
# 7. len() FUNCTION POLYMORPHISM
# ======================================================

print("\n7. len() FUNCTION POLYMORPHISM")
print("-" * 70)

print("len('Python') =", len("Python"))
print("len([10, 20, 30]) =", len([10, 20, 30]))
print("len({'a': 1, 'b': 2}) =", len({"a": 1, "b": 2}))

"""
Same len() function works differently:
string -> number of characters
list -> number of items
dictionary -> number of keys
"""


# ======================================================
# 8. CUSTOM OPERATOR POLYMORPHISM USING __add__
# ======================================================

print("\n8. CUSTOM OPERATOR POLYMORPHISM USING __add__")
print("-" * 70)


class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def show(self):
        print(f"Total money: ₹{self.amount}")


m1 = Money(100)
m2 = Money(200)

m3 = m1 + m2
m3.show()


# ======================================================
# 9. METHOD OVERLOADING STYLE IN PYTHON
# ======================================================

print("\n9. METHOD OVERLOADING STYLE IN PYTHON")
print("-" * 70)

"""
Python does not support true method overloading like Java/C++.

This will NOT work as overloading:

def add(a, b):
    return a + b

def add(a, b, c):
    return a + b + c

The second function replaces the first one.

Instead, Python uses default arguments or *args.
"""


class Calculator:
    def add(self, a=0, b=0, c=0):
        return a + b + c


calc = Calculator()

print("add(10, 20) =", calc.add(10, 20))
print("add(10, 20, 30) =", calc.add(10, 20, 30))


# ======================================================
# 10. POLYMORPHISM USING *args
# ======================================================

print("\n10. POLYMORPHISM USING *args")
print("-" * 70)


class FlexibleCalculator:
    def add(self, *numbers):
        total = 0
        for number in numbers:
            total += number
        return total


fc = FlexibleCalculator()

print("add(1, 2) =", fc.add(1, 2))
print("add(1, 2, 3, 4, 5) =", fc.add(1, 2, 3, 4, 5))


# ======================================================
# 11. REAL-WORLD EXAMPLE: NOTIFICATION SYSTEM
# ======================================================

print("\n11. REAL-WORLD EXAMPLE: NOTIFICATION SYSTEM")
print("-" * 70)


class EmailNotification:
    def send(self, message):
        print(f"Email sent: {message}")


class SMSNotification:
    def send(self, message):
        print(f"SMS sent: {message}")


class WhatsAppNotification:
    def send(self, message):
        print(f"WhatsApp message sent: {message}")


def send_alert(notification_service, message):
    notification_service.send(message)


send_alert(EmailNotification(), "Your order has been shipped.")
send_alert(SMSNotification(), "Your OTP is 123456.")
send_alert(WhatsAppNotification(), "Meeting starts at 5 PM.")


# ======================================================
# 12. BENEFITS OF POLYMORPHISM
# ======================================================

print("\n12. BENEFITS OF POLYMORPHISM")
print("-" * 70)

print("""
1. Same method name can be used for different classes.
2. Code becomes flexible and reusable.
3. Reduces unnecessary if-else conditions.
4. Makes code easier to extend.
5. Important for clean object-oriented design.
""")


# ======================================================
# 13. INTERVIEW DEFINITION
# ======================================================

print("\n13. INTERVIEW DEFINITION")
print("-" * 70)

print("""
Polymorphism is an OOP concept where the same interface,
such as a method, function, or operator, behaves differently
depending on the object using it.

Example:
Dog.sound() -> Bark
Cat.sound() -> Meow

Same method name: sound()
Different behavior: Bark / Meow
""")
