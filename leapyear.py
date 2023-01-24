# write a program to find wheather a given year is leapyear of not?
year = int(input("Enter a year : "))

if year % 4 == 0:
    print("The year is leapyear.")

elif year % 400 == 0:
    print("The year is leapyear.")

elif year % 100 == 0:
    print("The year is not leapyear.")

else:
    print("The year is not leapyear.")



