months={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
def leapyear(year):
    return year%400==0 or year%4==0
#format for date: [day,month,year]
def dayNumber(date):
    days=0
    newDict=months.copy()
    if(leapyear(date[2])):
        newDict[2]=29
    for month in range(1,date[1]):
        days+=newDict[month]
    days+=date[0]
    return days

def daysFrom(date):
    cursor=date
    days=dayNumber(date)-1
    for year in range(1900,date[2]):
        days+=dayNumber([31,12,year])
    return days

date=[1,1,1900]
sundays=0
while(not date==[31,12,1999]):
    if(leapyear(date[2])):
        months[2]=29
    else:
        months[2]=28
    date[0]+=1
    if(date[0]>months[date[1]]):
        date[0]=1
        date[1]+=1
    if(date[1]>12):
        date[1]=1
        date[2]+=1
    if((daysFrom(date)-1)%7==0 and date[0]==1):
        sundays+=1
print(sundays)