import re
def split_a_string(txt):
    change=""
    pattern8=re.compile(r'[A-Z][a-z]+')
    words=pattern8.findall(txt)
    for i,word in enumerate(words):
        if i!=0:
            change+= " " + word
        else:
            change+=word
    return change

print(split_a_string("ZhasghjFihgjUbbn"))