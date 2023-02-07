
from colorama import init
from colorama import Fore, Back, Style
init()
print(Fore.BLACK )
print(Back.GREEN)

what = input("what we need to do? (+,-): ")
print(Back.CYAN)

a = float(input("first digit: "))
b = float(input("second digit: "))
print(Back.RED)
if what=="+":
    c=a+b
    print("Pesult: " + str(c))
elif what=="-":
    c=a-b    
    print("Pesult: " + str(c))
else:
    print("Operation error")    
input()    