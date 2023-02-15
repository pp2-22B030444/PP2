from datetime import date , timedelta
dt = date.today()-timedelta(1)
dr = date.today()+timedelta(1)
print('Current Date :', date.today())
print('Yesterday :', dt)
print('Tomorrow :', dr)