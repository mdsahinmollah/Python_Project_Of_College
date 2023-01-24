num1 = int(input("enter 1'st number : "))
num2 = int(input("Enter 2'nd number : "))

if num1 > num2:
    lcm = num1

else:
    lcm = num2

while True:
    if lcm % num1 == 0 and lcm % num2 == 0:
        break
    else:
        lcm = lcm + 1

print(f"LCM of {num1} and {num2} is",lcm)