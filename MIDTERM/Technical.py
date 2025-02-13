def palindrome(number):
    number_str = str(number)
    return number_str == number_str[::-1]

def process_numbers(file_name):
    try:
        file = open(file_name, 'r')
        lines = file.readlines()
        file.close()

        line_number = 1
        for line in lines:
            numbers = line.strip().split(',')
            numbers = [int(num) for num in numbers]
            total = sum(numbers)
            if palindrome(total):
                status = "Palindrome"
            else:
                status = "Not a palindrome"
            print(f"Line {line_number}: {', '.join(map(str, numbers))} (sum {total}) - {status}")
            line_number += 1
    except FileNotFoundError:
        print("File not found! Make sure 'numbers.txt' exists.")
    except ValueError:
        print("Error: Ensure the file contains only valid numbers separated by commas.")

process_numbers("numbers.txt")
