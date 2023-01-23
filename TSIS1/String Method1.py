txt = "Hello, welcome to my world."

x = txt.endswith(".")

print(x)

txt = "H\te\tl\tl\to"

x =  txt.expandtabs(2)

print(x)

txt = "H\te\tl\tl\to"

print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))

txt = "Hello, welcome to my world."

x = txt.find("welcome")

print(x)


txt = "Hello, welcome to my world."

x = txt.index("welcome")

print(x)

txt = "Hello, welcome to my world."

x = txt.index("e", 5, 10)

print(x)

txt = "Company12"

x = txt.isalnum()

print(x)

txt = "Company 12"

x = txt.isalnum()

print(x)
txt = "CompanyX"

x = txt.isalpha()

print(x)
txt = "Company123"

x = txt.isascii()

print(x)