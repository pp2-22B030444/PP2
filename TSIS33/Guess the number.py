import random
x=(random.randrange(1,20))

print('Hello! What is your name?')
a=input()
print()
p='Well, {}, I am thinking of a number between 1 and 20.'
print(p.format(a))
print('Take a guess.')
b=int(input())
print()
cnt=0
while b!=x:
    if b<x:
      cnt+=1
      print('Your guess is too low.')
      print('Take a guess.')
      b=int(input())
      print()
    if b>x:
       cnt+=1
       print('Your guess is too up.')
       print('Take a guess.')
       b=int(input()) 
       print()
    if x==b:
        print('Good job, ' + str(a) +  '! You guessed my number in '+ str(cnt)+ ' guesses!')

         