txt = "python is FUN!"

print(txt.capitalize())
txt = "Hello, And Welcome To My World!"

print(txt.casefold())
txt = "banana"

print(txt.center(20))
txt = "banana"

print(txt.center(20,"O"))
txt = "I love apples, apple are my favorite fruit"

print(txt.count("apple"))
txt = "I love apples, apple are my favorite fruit"

print(txt.count("apple", 10, 24))
txt = "My name is Ståle"

print(txt.encode())
txt = "My name is Ståle"

print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))