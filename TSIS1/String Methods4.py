txt = "apple, banana, cherry"

x = txt.rsplit(", ")

print(x)
txt = "     banana     "

x = txt.rstrip()

print("of all fruits", x, "is my favorite")
txt = "welcome to the jungle"

x = txt.split()

print(x)
txt = "apple#banana#cherry#orange"

x = txt.split("#")

print(x)
txt = "Thank you for the music\nWelcome to the jungle"

x = txt.splitlines(False)

print(x)
txt = "Hello, welcome to my world."

x = txt.startswith("wel", 7, 20)

print(x)
txt = ",,,,,rrttgg.....banana....rrr"

x = txt.strip(",.grt")

print(x)
txt = "Hello My Name Is PETER"

x = txt.swapcase()

print(x)
txt = "Welcome to my world"

x = txt.title()

print(x)
#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}

txt = "Hello Sam!"

print(txt.translate(mydict))
txt = "Hello my friends"

x = txt.upper()

print(x)
txt = "50"

x = txt.zfill(10)

print(x)