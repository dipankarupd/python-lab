# Write a python program to accept a sequence of whitespace 
# separated words as input and
# prints the words after removing all duplicate words and sorting 
#them alphanumerically.


def main():

    sentence = input('Enter the sentnce: ')
    my_set = {}

    my_set = sentence.split()
