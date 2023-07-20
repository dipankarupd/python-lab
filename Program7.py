'''Solve the following using Recursion:
a) find the length of a string
b) find the smallest element in a list
'''
def length(word):
    if(word == ''):
        return 0
    return 1 + length(word[1:])

def find_smallest(my_list,n):
    

    if(n < 0):
        return None

    smallest = my_list[n-1]
    small = find_smallest(my_list,n-1)
    if(small is not None and small < smallest):
        smallest = small
    return smallest

def main():
    word = input('Enter the valid name: ')
    print(length(word))

    my_list = list()
    n = int(input('Enter the number of elements in the list: '))
    for i in range(0,n):
        elem = int(input('Enter the element: '))
        my_list.append(elem)
    
    print(find_smallest(my_list,n))

main()