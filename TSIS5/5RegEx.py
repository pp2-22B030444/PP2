import re
pattern5 = re.compile(r"a.+b\Z")
print('Task5')
print(pattern5.search("adfghjkb"))
print(pattern5.search('sdfgh'))
print(pattern5.search('aaaaaabbbbb'))
