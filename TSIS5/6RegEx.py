import re
pattern6=re.compile(r"[ .,]")
print('Task 6')
txt="dfgh hj m, huhhi.., huhu .,"
print(pattern6.sub(":",txt ))