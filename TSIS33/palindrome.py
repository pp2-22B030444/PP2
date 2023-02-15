def pel(s):
    str=s[::-1]
    print(str)
    if s==str:
        print("string is palindrome")
    else:
        print("string is not polindrome")
    
a=input()
print(pel(a))