print("+ - addition", "- - subtraction", "* - multiplication", "/ - division", "^ - exponentiation", "# - square root", "% - conversion to percentages")
choice = input("Pick what You want to do: ")
if (choice == "+"):
    firstNum = int(input("Enter first number: "))
    secondNum = int(input("Enter second number: "))
    result = firstNum + secondNum
    print("Your result is",result )
if (choice == "-"):
    firstNum = int(input("Enter first number: "))
    secondNum = int(input("Enter second number: "))
    result = firstNum - secondNum
    print("Your result is", result)
if (choice == "*"):
    firstNum = int(input("Enter first number: "))
    secondNum = int(input("Enter second number: "))
    result = firstNum * secondNum
    print("Your result is", result)
if (choice == "/"):
    firstNum = int(input("Enter first number: "))
    secondNum = int(input("Enter second number: "))
    if (secondNum == 0):
        print("Do not divide by 0!!!")
    else:
        result = firstNum / secondNum
        print("Your result is", result)