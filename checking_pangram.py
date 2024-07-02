"""
QUESTION FOUR

Design a function that determines whether a given string is a pangram. A 
pangram is a sentence or phrase containing every letter of the alphabet at 
least once. Punctuation and case are typically ignored. For example, the 
string "The quick brown fox jumps over the lazy dog" is a pangram, while 
"Hello, world!" is not.3.
"""""
import string
def is_pangram(sentence):
    sentence = sentence.lower()
    sentence = ''.join(char for char in sentence if char.isalpha())
    alphabet = set(string.ascii_lowercase)
    return set(sentence) >= alphabet
def check_pangram_input():
    while True:
        user_input = input("Enter a sentence (enter '0' to terminate): ")
        if user_input == '0':
            break
        if is_pangram(user_input):
            print(f'"{user_input}" is a pangram.')
        else:
            print(f'"{user_input}" is not a pangram.')
check_pangram_input()
