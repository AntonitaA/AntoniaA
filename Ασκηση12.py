import datetime
#from dateutil import relativedelta
from calendar import monthrange

date_str = input("Δώσε μία ημερομηνία σε μορφή ΗΗ/ΜΜ/ΕΕΕΕ: ")
#στοιχεία που δίνει ο χρήστης
y = datetime.datetime.strptime(date_str, "%d/%m/%Y")
day1 = int(y.strftime("%d"))
month1 = int(y.strftime("%m"))
year1 = int(y.strftime("%Y"))

#τρέχοντα στοιχέια ημερομηνίας και ώρας
x = datetime.datetime.utcnow() + datetime.timedelta(hours=2) #η τρέχουσα ημερομηνία και ώρα διαμορφωμένη σύμφωνα με το time zone
year_curr = int(x.strftime("%Y")) #το τρέχον έτος
month_curr = int(x.strftime("%m")) #ο τρέχων μήνας
day_curr = int(x.strftime("%d")) #η τρέχουσα μέρα
hour_curr = int(x.strftime("%H")) #η τρέχουσα ώρα
seconds_curr = int(x.strftime("%S")) #τα τρέχοντα δευτερόλεπτα

years = abs(year1 - year_curr)
print(years)

daysy = 0
for i in range(years-1):
    if (year1 <= year_curr):
        if ((year1+i)%4 == 0 or (year1+i)%400 == 0 and (year1+i)%100 != 0):
            daysy = daysy + 366
        else:
            daysy = daysy + 365
    else:
        if((year_curr+i)%4 == 0 or (year_curr+i)%400 == 0 and (year_curr+i)%100 != 0):
            daysy = daysy + 366
        else:
            daysy = daysy + 365
print(daysy)

#υπολογίζει πόσοι μήνες μεσολλαβούν ανάμεσα στις ημερομηνίες
if (year1 > year_curr):
    mon = abs(month1 - month_curr + 12)
elif (year1 == year_curr):
    mon = abs(month1 - month_curr)
else:
    mon = abs(month1 - month_curr - 12)
print(mon)

#υπολογίζει πόσοι ολόκληρες μήνες μεσολλαβούν μεταξή των ημερομηνιών
daysm = 0
i = 1
m = monthrange(year1, month1)[1]
if (year1 < year_curr):
    while(month1+i <= 12):
        daysm = daysm + int(monthrange(year1, month1+i)[1])
        i += 1
    for j in range (1, month_curr-1):
        daysm = daysm + int(monthrange(year_curr, j)[1])
    if (month_curr-1 == 1):
        daysm = daysm + 31
elif (year1 > year_curr):
    while (month_curr+i <= 12):
        daysm = daysm + int(monthrange(year_curr, month_curr+i)[1])
        i += 1
    for j in range(1, month1):
        daysm = daysm + int(monthrange(year1, j)[1])

print(daysm)

#υπολογίζει τις υπόλοιπες μέρες των μη ολόκληρων μηνών, δηλαδή τις ημέρες του μήνα που έχει δώσει ο χρήστης και τις μέρες του τρέχοντος μήνα
daysm1  = 0
if (mon == 0 and year1 == year_curr):
    daysm1 = abs(day1 - day_curr)
if (year1 < year_curr):
    daysm1 = (int(m) - day1) + day_curr - 1
if (year1 > year_curr):
    daysm1 = (int(monthrange(year_curr, month_curr)[1]) - day_curr) + day1 - 1
    
print(daysm1)


day = daysy + daysm + daysm1
if (day1 == day_curr and month1 == month_curr and year1 == year_curr):
    hours = 0
    seconds = 0
else:
    hours = 24 - int(hour_curr)
    seconds = 3600 - int(seconds_curr)

print("Η δοσμένη ημερομηνία απέχει " + str(day) + " ημέρα-ες " + " / " + str(hours) + " ώρα-ες " + " / " + str(seconds) + " δευτερόλεπτο-α από σήμερα")
print("Ο μήνας της δοσμένης ημερομηνίας έχει " + str(m) + "ημέρες")