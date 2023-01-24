#find out vowels, consonant, and space..keyword

a = input("Enter any word : ")
consonent = 0
space = 0
vowel = 0
for i in a :
    if(i == "A" or i == "E" or i == "I" or i == "O" or i == "U"):
        vowel += 1
    elif(i == "B",i== "C",i == "D",i == "F",i == "G",i == "H",i  == "J",i == "K",i == "L",i == "M",i == "N",
    i == "P",i == "Q",i == "R",i == "S",i == "T",i == "V",i == "W",i == "X",i == "Y",i == "Z"):
    consonent += 1

    else:
        space += 1


print("> Total vowels are : ",vowel)
print("> Total spaces are : ",space)
print("> Total consonants are : ",consonent)