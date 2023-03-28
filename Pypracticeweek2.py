def is_leap(year):
    #leap = False
    if 1900 <= year <= 10**5:
        if (year%4 == 0 and year%100 != 0) or (year%100 ==0 and year%400 ==0):
            leap = True 
        else:
            leap = False
    
    print(leap)

#year = int(input("Enter a year:"))
is_leap(1994)
