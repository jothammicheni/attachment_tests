"""
QUESTION Two
Write a recursive function to calculate the factorial of a number
"""

def Calculate_factorial():
  while True:
    try:
        number = int(input("Enter a non-negative integer to find the factorial or type 00 to Quit: "))
        if number==00:
            break
        elif number < 0:
            print("Undefine factorial for negative numbers.")
            break
        elif number == 0:
            print("Factorial of 0 is 1.")
        else:
            factorial = 1
            for i in range(1, number + 1):
                factorial *= i
            print(f"Factorial of {number} is :")
            print(factorial)
    except ValueError:
        print("Invalid input. Please enter a valid non-negative integer or type 0 to quit.")

# Driver Code
Calculate_factorial()
