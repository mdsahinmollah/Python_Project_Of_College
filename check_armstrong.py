n = float(input("Enter a number : "))

sum = 0
temp =n

while n>0:
    digit = n%10
    sum = sum + digit ** 3
    n = n//10

if temp==sum:
    print(f"{temp} is armstrong number.")

else:
    print(f'{temp} is not armstromg number')