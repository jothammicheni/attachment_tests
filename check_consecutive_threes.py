"""
QUESTION FIVE

Design a function that takes a list of integers as input. The function should
return True if the list contains two consecutive threes (3 next to a 3) anywhere
within the list. Otherwise, it should return False. For example, the function
should return True for [1, 3, 3] and False for [1, 3, 1, 3].
"""
def check_consecutive_threes(list):
    for i in range(len(list)-1):
        if list[i] == 3 and list[i+1] == 3:
            print("Consecutive threes found")
            return
    print("No consecutive threes found")

while True:
    user_input = input("Enter a list of numbers SEPARATED BY SPACES (or 0 to exit): ")
    if user_input == "0":
        print("Exiting program...")
        break
    numbers = [int(num) for num in user_input.split()]
    check_consecutive_threes(numbers)
