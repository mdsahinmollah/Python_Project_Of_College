#write a program wheather a person is eligible for giving vote or not? Display how many years left to be eligible?

age = int(input("Enter a number : "))

if(age>18):

    print("He/She is eligible for giving vote.")
else:
    print("He/She is not eligible for giving vote.")

    if(age<18):

        a = 18 - age

        print(f"After {a} years he/she will eligible for giving vote.")