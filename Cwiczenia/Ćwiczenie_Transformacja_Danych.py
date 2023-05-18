numbers = (numbers
           for numbers in range (2,471)
           if (numbers % 7 == 0)
           if (numbers % 5 != 0))
for item in numbers:
    print(item)