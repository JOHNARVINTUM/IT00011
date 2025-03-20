def divide(num1, num2):
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
        return None
    return num1 / num2


def powerOf(num1, num2):
    return num1 ** num2


def remainder(num1, num2):
    if num2 == 0:
        print("Error: Division by zero is not allowed for remainder.")
        return None
    return num1 % num2


def summa(start, end):
    if start > end:
        print("Error: The second number must be greater than or equal to the first number.")
        return None
    return sum(range(start, end + 1))


def get_numbers():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        return num1, num2
    except ValueError:
        print("Invalid input. Please enter integers only.")
        return None, None


def menu():
    while True:
        print("\nChoose an operation:")
        print("[D] - Divide")
        print("[E] - Exponentiation")
        print("[R] - Remainder")
        print("[F] - Summation")
        print("[Q] - Quit")

        choice = input("Enter your choice: ").strip().upper()

        if choice == "Q":
            print("Exiting program. Goodbye!")
            break

        num1, num2 = get_numbers()
        if num1 is None or num2 is None:
            continue

        if choice == "D":
            result = divide(num1, num2)
        elif choice == "E":
            result = powerOf(num1, num2)
        elif choice == "R":
            result = remainder(num1, num2)
        elif choice == "F":
            result = summa(num1, num2)
        else:
            print("Invalid choice. Please choose a valid option.")
            continue

        if result is not None:
            print(f"Result: {result}")



menu()
