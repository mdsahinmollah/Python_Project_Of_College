
#find out alphabets, numbers, and spaces......

s = input("Enter your college name : ")
a = 0
b = 0
c = 0
for i in s:
    if(i.isalpha()):
        a += 1
        print("> Alphabets are : ",a)
    elif(i.isdigit()):
        b += 1
        print("> The numbers are : ",b)
    else:
        c+= 1
        print("> The spases are : ",c)