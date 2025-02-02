#TECHNINAL_1.1

string = input("Enter a String: ")
vowel = 0
space = 0
consonant = 0
print("")


for i in range(len(string)):
    if string[i] == "A" or string[i] == "a": vowel += 1
    if string[i] == "E" or string[i] == "e": vowel += 1
    if string[i] == "I" or string[i] == "i": vowel += 1
    if string[i] == "O" or string[i] == "o": vowel += 1
    if string[i] == "U" or string[i] == "u": vowel += 1

for i in range(len(string)):
    if string[i] == "A" or string[i] == " ": space += 1

print("Number of vowels in the string: " + str(vowel))
print("Number of spaces in the string: " + str(space))
print("Number of consonants in the string: " + str(len(string) - vowel - space))









