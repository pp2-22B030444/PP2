import re
def snake_to_camel(txt):
    change=""
    pattern8=re.compile(r"[_]")
    words=pattern8.split(txt)
    for i , word in enumerate(words):
        if i!=0:
            change+=word.capitalize()
        else:
            change+=word
    return change

print(snake_to_camel('Zhasmin_is_power'))