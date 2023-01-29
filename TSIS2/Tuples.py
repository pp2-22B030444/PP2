thistuple = ("apple", "banana", "cherry")
print(thistuple)
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)