import re
def insert_spaces(txt):
    change=""
    pattern8=re.compile(r'[A-Z][a-z]+')
    words=pattern8.findall(txt)
    for i,word in enumerate(words):
        if i!=0:
            change+= " " + word
        else:
            change+=word
    return change

print(insert_spaces("ZhasghjFihgjUbbn"))