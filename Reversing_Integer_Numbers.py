"""
QUESTION One
Design a function that reverses the digits of an integer. For example, 50
should become 5 and -12 should become -21.
"""

def reverse_integer_number():
    while True:
        try:
            number = int(input("Enter an integer ,(or type 0 to quit): "))
            if number == 0:
                print("Exiting program...")
                break

            # Handle numbers with negative values
            sign = -1 if number < 0 else 1
            number = abs(number)

            # Reverse the digits
            reversed_num = 0
            while number > 0:
                digit = number % 10
                reversed_num = reversed_num * 10 + digit
                number //= 10

            print(f"Reversed number is : {sign * reversed_num}")
        except ValueError:
            print("Invalid input. Please enter a valid integer or type 0 to quit.")



reverse_integer_number()
