#write a program to find out GCD of two numbers


a = int(input("Enter 1'st number :"))
b = int(input("Enter 2'nd number : "))
if(a<b):
    a,b = b,a
while(a%b):
    c = a % b
    a = b
    b = c

print(f"GCD of {a} and {b} is : ",b) 
