#write a program to convert the number in reverse.........

num = int(input("> Enter a number : "))
rev = 0
while(num):
    rev = rev * 10 + num % 10
    num = num // 10
else:
    print("> Reverse number is : ",rev)