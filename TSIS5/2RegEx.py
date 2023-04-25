import re
pattern1=re.compile(r"ab{1,4}")
print('Task2')
print(pattern1.findall('aaaaabsahdaaabbbjbsbabbbb'))