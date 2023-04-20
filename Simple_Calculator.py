print("+ - addition", "- - subtraction", "* - multiplication", "/ - division", "^ - exponentiation", "# - square root", "% - conversion to percentages")
choice = input("Pick what You want to do: ")
if (choice == "+"):
    firstNum = int(input("Enter first number: "))
    secondNum = int(input("Enter second number: "))
    result = firstNum + secondNum
    print("Your result is",result )
