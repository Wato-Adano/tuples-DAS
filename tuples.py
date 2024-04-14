# Howto access items in tuples
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# creating tuples
thistuple = ("apple", "banana", "cherry")
print(type(thistuple))

# Adding items in tuples
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)


# printing each items
for y in thistuple:
    print(y)
    
    # finding length in tuples
    
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
