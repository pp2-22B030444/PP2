def ispalindrome(n):
    s=n[::-1]
    if n==s:
        return True
    else:
        return False
a=input()
print(ispalindrome(a))