#write a progam to find out the greatest number among three numbers......with Nested if-else

a = int(input("Enter a number : "))
b= int(input("Enter a number : "))
c = int(input("Enter a number : "))

if(a>b):
    if(a>c):
        print(f" {a} is greater than {b} & {c}")

    else:
        print(f" {c} is greater than {a} & {b}")
else:
    if(b>c):
        print(f" {b} is greater than {a} & {c}")
    else:
        print(f" {c} is greater than {a} & {b}")
