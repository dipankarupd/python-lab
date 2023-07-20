"""
write a python program to read a string of 4 
char from user. convert each char in the string to its 
next alphabet
eg:  a b c d -> b c d e
"""


def next(char):
    if char == 'z':
        return a
    else:
        return chr(ord(char)+1)


def main():
    value = input("enter the string")
    if len(value) != 4:
        print("invalid input")

    new_str = ""

    for val in value:
        new_str += next(val)

    print(new_str)  

main()

    