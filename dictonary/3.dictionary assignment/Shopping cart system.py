# Shopping Cart System
# Create cart dictionary example :
# cart = {
#     "Laptop": {"price": 50000, "qty": 1},
#     "Mouse": {"price": 500, "qty": 2}
# }
# Tasks:
# Add product
# Update quantity
# Remove product
# Calculate total bill
# Find most expensive product
# Apply 10% discount if total > 50000

cart = {
    "Laptop": {"price": 50000, "qty": 1},
    "Mouse": {"price": 500, "qty": 2}
}


# Add product

cart.update({
    "printer": {
        "price": 5000,
        "qty": 3
    }
})

print("After adding printer:")
print(cart)


# Update quantity

cart["printer"]["qty"] = 5

print("\nAfter updating quantity:")
print(cart)


# Remove product

del cart["printer"]

print("\nAfter deleting printer:")
print(cart)


# Calculate total bill

total = 0

for itm in cart:

    total += cart[itm]["price"] * cart[itm]["qty"]

print("\nTotal Bill:")
print(total)

# Output:
# 51000




# Find most expensive product

maxi = 0
expensive = ""

for itm in cart:

    if cart[itm]["price"] > maxi:

        maxi = cart[itm]["price"]
        expensive = itm

print(expensive)

# Output:
# Laptop





# Apply 10% discount if total > 50000

if total > 50000:

    discount = total * 0.10
    final_bill = total - discount
    print("Discount Applied:", discount)
    print("Final Bill:", final_bill)

else:
    print("\nNo discount applied")