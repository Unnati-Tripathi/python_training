# Tuple in Python

# A tuple is similar to a list, but its values cannot be changed after creation.

# Features of Tuple
# Ordered
# Unchangeable (Immutable)
# Allows duplicate values
# Written using parentheses ()


colors = ("red", "green", "blue")
print(colors)
# ('red', 'green', 'blue')



# Accessing Elements
print(colors[1])
# green


# Tuple Cannot Be Modified
colors[1] = "yellow"
# This gives an error because tuples are immutable.