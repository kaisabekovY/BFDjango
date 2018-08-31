def is_leap(year):
    leap = True
    notleap = False
    if (year%4==0 | year%400==0):
        return leap
    elif (year%100==0):
        return notleap
    else:
        return notleap

year = int(input())
print(is_leap(year))
