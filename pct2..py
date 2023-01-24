#3  Write a program to find out thee area of a triangle...

# a = float(input("Enter the base : "))
# b = float(input("Enter the height : "))
# formula = 0.5 * a * b
# print(formula)



#5 Write a program to swap values of two variables.......

# x = int(input("Enter any name or number : "))
# y = int(input("Enter any name or number : "))

# x,y = y,x

# print("The value of x by swappiing into y is : ",x)
# print("The value of y by swappiing into x is : ",y)

#4  Write a program to solve quadratic equation........

# import cmath

# print("General form : ax^2+bx+c = 0")

# a = int(input("Enter a : "))
# b = int(input("Enter b : "))
# c = int(input("Enter c : "))

# d = (b**2)-(4*a*c)

# soln1 = (-b-cmath.sqrt(d))/(2*a)
# soln2 = (-b+cmath.sqrt(d))/(2*a)

# print("\n")
# print(f"result of equation,{a}x^2+{b}x+{c} = 0, are : ")

# print(f"The solutions are : {soln1}and {soln2}")


#6  write a program to convert kilometer to miles...

# km = float(input("enter Kilometer : "))
# f = km * 0.62137119
# print(f"The Equivalent of {km} km in miles is : ",f,('miles'))

#7   write a program to convert celcius to fahrenheit...[T(fahrenheit) = (T)(Celcius)*9/5+32]


# c = float(input("Enter the celcius temperature : "))
# f = (c*9/5)+32
# print("the fahrenheit temperaure is : ",f)


#8  Write a program to calculate simple interest.....[(p*r*t)/100]

# p = float(input("Enter the principle amount : "))
# r = float(input("Enter the rate of interest : "))
# t = float(input("Enter the time : "))

# formula = (p*r*t)/100
# print(formula)

#9  Write a program to calculate the compound interest...[A = P(1+R/100)^t]  A=amont,p= priciple,r= rate,t= time.

# p = float(input("Enter the principle amount : "))
# r = float(input("Enter the rate : "))
# t = float(input("Enter the time : "))
# a = p*(1+(r/100))**t
# ci= a-p  #a = amount, p = principle amount



# print("The compound interest is : ",ci)



#10 write a program to show a calender   month & year...


import calendar

y = int(input("enter year : "))
m = int(input("enter month : "))
d = int(input("enter day : "))   #day is exceptional

print(calendar.month(y,m))