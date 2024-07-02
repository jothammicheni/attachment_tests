
"""
QUESTION THREE

Design a function that takes a string or sequence of characters as input and
returns the character that appears most frequently.;
//Eg 11189 => '1'
//hello => l
"""
def frequent_char(string):
    while True:
        try:
            string= input("Enter a string or enter 0 to exit: ")
            if string == "0":
                print("Exiting program...")
                break

            character_count= {}
            for char in string:
                character_count[char] = character_count.get(char, 0) + 1
            max_character= max(character_count, key=character_count.get)

            if character_count[max_character] == 1:
                print("No frequent character found.")
            else:
                print(f"The most frequent character in '{string}' is:")
                print( max_character)
        except ValueError:
            print("Enter a valid string.")

frequent_char("")
