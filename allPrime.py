lower = int(input("Enter lower value : "))
upper = int(input("Enter upper value : "))

print(f'Prime numbers between {lower} & {upper} is : ')

for i in range(lower,upper + 1):
    if i > 1:
        for num in range(2,i):
            if i % num == 0:
                break
        else:
            print(i)
