#Write a program to calculate the sum & average of numbers from m to n.

n = int(input("Enter Number : "))
sum = 0
for i in range(1, n + 1):
    sum = sum + i

print(f"sum of first {n} numbers is :", sum)

average = sum / n
print(f"Average of {n} numbers is : ", average)