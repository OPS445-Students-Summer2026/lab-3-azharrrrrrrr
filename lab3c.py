#!/usr/bin/env python3
'''Lab 3 Inv 2 function operate '''
# Author ID: aashaikh9

def operate(number1, number2, operator):
    if operator == 'add':
        return number1 + number2
    elif operator == 'subtract':
        return number1 - number2
    elif operator == 'multiply':
        return number1 * number2
    else:
        return 'Error: function operator can be "add", "subtract", or "multiply"'

if __name__ == '__main__':
    print(operate(10, 5, 'add'))
    print(operate(10, 5, 'subtract'))
    print(operate(10, 5, 'multiply'))
    print(operate(10, 5, 'divide'))

import lab3c
lab3c.operate(10, 20, 'add')
# Will return 30
lab3c.operate(2, 3, 'add')
# Will return 5
lab3c.operate(100, 5, 'subtract')
# Will return 95
lab3c.operate(10, 20, 'subtract')
# Will return -10
lab3c.operate(5, 5, 'multiply')
# Will return 25
lab3c.operate(10, 100, 'multiply')
# Will return 1000
lab3c.operate(100, 5, 'divide')
# Will return Error: function operator can be "add", "subtract", or "multiply"
lab3c.operate(100, 5, 'power')
# Will return Error: function operator can be "add", "subtract", or "multiply"
