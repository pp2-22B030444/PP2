from datetime import datetime
def difference(dt,dr):
    timdelta=dt-dr
    return timdelta.days*24*60*60+timdelta.seconds
date1 = datetime.strptime('2017-02-14 01:00:00', '%Y-%m-%d %H:%M:%S')
date2 = datetime.now()
print(difference(date2,date1), 'seconds')