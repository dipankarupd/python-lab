def next(ch):
    if ch == 'z':
        return 'a'
    arr = [i for i in range ((97), (97+26+1))]
    for i in arr:
        if chr(i) == ch:
            return chr(i+1)
     



def main():
    str = input('Enter the char: ')

    newstr = ""
    for i in str:
        newstr = newstr + next(i)
    print(newstr)

main()