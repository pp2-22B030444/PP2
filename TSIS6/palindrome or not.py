def check(s):
    n=s[::-1]
    if n==s:
        return True
    else:
        return False
s=input('Check the word:')
print(check(s))