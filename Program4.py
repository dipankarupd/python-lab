def pattern(n):
    x = 1
    for i in range (1,n+1):
        
        for j in range (1, (2*i)):
            print(chr(x+64), end = " ")
            x = x + 1
        print()

pattern(5)