num1 = 0.0
num2 = 0.0
num3 = 0.0

while True:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    if num1 >= num2:
        if num1 >= num3:
            print("The first number is the greatest")
            if num2 >= num3:
                print("Numbers in descending order:", [num1, num2, num3])
            else:
                print("Numbers in descending order:", [num1, num3, num2])
        else:
            print("The third number is the greatest")
            print("Numbers in descending order:", [num3, num1, num2])
    else:
        if num2 >= num3:
            print("The second number is the greatest")
            if num1 >= num3:
                print("Numbers in descending order:", [num2, num1, num3])
            else:
                print("Numbers in descending order:", [num2, num3, num1])
        else:
            print("The third number is the greatest")
            print("Numbers in descending order:", [num3, num2, num1])