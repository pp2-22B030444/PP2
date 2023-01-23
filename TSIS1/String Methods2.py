a = "\u0030" #unicode for 0
b = "\u0047" #unicode for G

print(a.isdecimal())
print(b.isdecimal())
txt = "50800"

x = txt.isdigit()

print(x)
txt = "Demo"

x = txt.isidentifier()

print(x)
txt = "hello world!"

x = txt.islower()

print(x)
txt = "565543"

x = txt.isnumeric()

print(x)
txt = "Hello! Are you #1?"

x = txt.isprintable()

print(x)
txt = "   "

x = txt.isspace()

print(x)
txt = "Hello, And Welcome To My World!"

x = txt.istitle()

print(x)
txt = "THIS IS NOW!"

x = txt.isupper()

print(x)