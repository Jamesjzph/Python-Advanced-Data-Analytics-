try:
    a = int(input("Enter a number: "))
    b = int(input("Enter second number: "))
    r = a / b
except ZeroDivisionError:
    print("Error: You can't divide by zero!")
except ValueError:
    print("Error: Please enter whole numbers only.")
else:
    print("The result is", r)
finally:
    print("Execution Completed!!")