a = int(input('Enter first number : '))
b = int(input('Enter second number : '))
op = input('Enter the operator(eg. +,-,*,/,%) : ')

if op is '+':
    print(a + b)
elif op is '-':
    print(a - b)
elif op is '*':
    print(a * b)
elif op is '/':
    print(a / b)
elif op is '%':
    print(a % b)
else:
    print('Wrong input')