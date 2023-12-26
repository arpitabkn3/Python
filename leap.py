year=int(input("enter the number"))
if(year % 400==0) and (year % 100==0):
    print("is leap year",year)
elif(year % 4==0) and(year %100!=0):
    print("is leap year",year)
else:
    print("is not year",year)
