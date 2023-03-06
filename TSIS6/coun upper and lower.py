import re
string=input()
upper=re.compile("[A-Z]")
lower=re.compile("[a-z]")
upper_pt = upper.findall(string)
lower_pt = lower.findall(string)
print(f'Num of lower chars {len(lower_pt)}')
print(f'Num of upper chars {len(upper_pt)}' )