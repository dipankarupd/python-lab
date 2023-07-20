"""
write a python program to simulate a simple calculator
"""

def calculator (op1, op2, op) :
    if op == '+':
        return op1 + op2
    elif op == '-' :
        return op1 - op2
    elif op == '*':
        return op1 * op2
    elif op == '/':
        if op2 == 0:
            print("invalid ")
            return -999999
        return op1/op2
    elif op == '^':
        return op1 ** op2


a = int(input("enter the operand 1:" ))
b = int(input("enter the operand 2:"))
operator = str(input("enter the operator"))

print(calculator(a,b,operator))