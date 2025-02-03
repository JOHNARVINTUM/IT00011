#Activity-2
num1 = int(input("Enter the First Term: "))
num2 = int(input("Enter the Last Term: "))

total = 0.0

if num1 < num2:
    for i in range(num1, num2 + 1):
        total += i

print(f"The sum of numbers from {num1} to {num2} is {total}.")

