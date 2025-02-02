#TECHNINAL_1.2

string = input("Enter a String: ")
sod = 0

for char in string:
    if char.isdigit(): 
        sod += int(char)  

print("The sum of the digits in the string is:", sod)
