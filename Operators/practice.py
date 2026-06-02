# Q1. Write a program to calculate final bill.
# If bill is greater than 5000, give 10% discount.

bill = 7000

if bill > 5000:
    discount = bill * 0.10
    final_bill = bill - discount
else:
    final_bill = bill

print("Final Bill:", final_bill)

# Output:
# Final Bill: 6300.0


# Q2. Check whether a number is even and greater than 10.

num = 24

if num % 2 == 0 and num > 10:
    print("Number is even and greater than 10")
else:
    print("Condition not satisfied")

# Output:
# Number is even and greater than 10


# Q3. Check whether student is eligible for scholarship.
# Conditions:
# marks greater than 80
# attendance greater than 75

marks = 85
attendance = 80

if marks > 80 and attendance > 75:
    print("Eligible for scholarship")
else:
    print("Not eligible for scholarship")

# Output:
# Eligible for scholarship


# Q4. Check whether a product is available in cart.

cart = ["Laptop", "Mouse", "Keyboard"]

if "Mouse" in cart:
    print("Product available")
else:
    print("Product not available")

# Output:
# Product available


# Q5. Compare two lists using == and is.

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)

# Output:
# True
# False

#finding the balance left in account after certain transtions..

account_balance = 5000

account_balance += 1500   # salary credited
account_balance -= 700    # electricity bill
account_balance += 2000   # bonus
account_balance -= 1000   # shopping

print(account_balance)