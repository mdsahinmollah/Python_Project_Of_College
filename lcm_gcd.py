a = float(input("Enter 1'st number : "))
b = float(input("Enter 2'nd number : "))
if a < b:
    a,b = b,a

m = a
n = b

while(a % b):
    c = a% b
    a = b
    b = c

print(f"GCD of {m} & {n} is :",b)

lcm = (m*n)/b

print(f"LCM of {m} & {n} is : ",lcm)