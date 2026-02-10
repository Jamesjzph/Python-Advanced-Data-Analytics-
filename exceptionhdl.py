def divide_numbers():
    try:
        num = float(input("Enter a number to divide 100 by: "))
        result = 100 / num
        
    except ZeroDivisionError:
        print("Error: You can't divide by zero!")
        
    except ValueError:
        print("Error: That wasn't a valid number.")
        
    else:
        print(f"Success! The result is {result}")
        
    finally:
        print("Execution complete. Cleaning up resources...")

divide_numbers()