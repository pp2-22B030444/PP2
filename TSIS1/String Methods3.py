myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)
txt = "banana"

x = txt.ljust(20)

print(x, "is my favorite fruit.")
txt = "banana"

x = txt.ljust(20, "O")

print(x)
txt = "Hello my FRIENDS"

x = txt.lower()

print(x)
txt = "     banana     "

x = txt.lstrip()

print("of all fruits", x, "is my favorite")
txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")
print(txt.translate(mytable))
txt = "I could eat bananas all day"

x = txt.partition("bananas")

print(x)
txt = "I like bananas"

x = txt.replace("bananas", "apples")

print(x)
txt = "Mi casa, su casa."

x = txt.rfind("casa")

print(x)
txt = "Mi casa, su casa."

x = txt.rindex("casa")

print(x)
txt = "banana"

x = txt.rjust(20)

print(x, "is my favorite fruit.")
txt = "banana"

x = txt.rjust(20, "O")

print(x)
txt = "I could eat bananas all day, bananas are my favorite fruit"

x = txt.rpartition("bananas")

print(x)