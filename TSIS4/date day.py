from datetime import date , timedelta
Yesterday = date.today()-timedelta(1)
Tomorrow = date.today()+timedelta(1)
print('Current Date :', date.today())
print('Yesterday :', Yesterday)
print('Tomorrow :', Tomorrow)