#write a program to find out the armstron number......

lower = int(input("Enter lower range : "))
upper = int(input("Enter upper range : "))

for num in range(lower,upper + 1):
    sum = 0
    i = num
    while i > 0 :
        digit = i%10
        sum+=digit ** 3
        i //= 10
        if num == sum :
            print("The armstrong number is : ",num)