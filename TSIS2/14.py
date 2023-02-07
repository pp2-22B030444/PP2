a=str(input('Which is the currency of Kazakhstan? '))
b=str(input('Name one of the past/present presidents of Kazakhstan: '))
c=str(input('What year Kazakhstan proclaim independence? '))
x=0
if a=='Tenge' or a=='KZT':
    x+=33.33
else:
    x+=0.00  
if b=='Tokaev' or b=='Nazarbaev':
    x+=33.33
else:
    x+=0.00
if c=='1991':
    x+=33.34
else:
    x+=0.00
y=str(x)
if x<70:
    print('You lost! You got only ' + y + '%' + ' correctness')
if x>70:
    print('Congrats, you won with ' + y + '0%' + ' correctness')