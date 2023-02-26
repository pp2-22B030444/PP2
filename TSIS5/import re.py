import re

#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")

import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

import re

#Return a list containing every occurrence of "ai":
#Возвращает список, содержащий каждое вхождение "ai":
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
import re

#The search() function returns a Match object:

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)

import re

txt = "The rain in Spain"

#Check if "Portugal" is in the string:

x = re.findall("Portugal", txt)
print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

