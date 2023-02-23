

def calculate(num1, num2, op = 'add'):
    op= op.lower()
    if op in ['a','add']:
        print(num1 + num2)
    elif op in ['m', 'multiply']:
        print(num1 * num2)
    elif op in ['s', 'subtract']:
        print(num1 - num2)
    else:
        print( 'Please enter another value ')

#example
print(calculate(10,10,'m'))