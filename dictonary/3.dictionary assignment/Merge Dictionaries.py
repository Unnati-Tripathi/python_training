# Merge and sort dictionary both by key and value
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

for key , val in d1.items():
    d2.update({key:val})

sorted(d2)
print(d2)
 