import re
def camel_to_snake(txt):
    change=""
    pattern10=re.compile(r"[A-Z][a-z]+")
    words=pattern10.findall(txt)
    for i,word in enumerate(words):
        if i!=0:
            change+= "_" + word.casefold()
        else:
            change+=word.casefold()
    return change
print(camel_to_snake('ZhasBurbon'))