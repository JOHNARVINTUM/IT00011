#TECHNINAL_1.3

num = 5
print("a.")
for i in range(1, num + 1):
    spaces = " " * (num - i) 
    numbers = ""
    for j in range(1, i + 1):
        numbers += str(j)
    print(spaces + numbers)


print("\nb.")
rows = 5
num = 1
i = 1

while i <= rows:
    j = 1
    output = ""
    while j < (2 * i):
        output += str(num)
        j += 1
    print(output)
    num += 2
    i += 1
