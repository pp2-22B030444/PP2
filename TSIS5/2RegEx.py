import re
pattern1=re.compile(r"ab{2,3}")
print('Task2')
print(pattern1.search('aaaaabsahdaaabbbjbsba'))