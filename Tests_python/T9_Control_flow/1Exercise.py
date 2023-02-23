num1=int(input('Enter number1: ').strip())
num2=int(input('Enter number2: ').strip())
operation=input('Enter operation: ').strip()


result=''

if operation =='+':
    result=num1+num2
elif operation == '-':
    result=num1-num2
elif operation == '*':
    result=num1*num2
elif operation == '/':
    if num2==0:
        print('This Is error value')
    else :
        result=num1 / num2
elif operation == '%':
    result=num1 % num2
else:
    print( 'Please enter another value ')

print(f'{num1} {operation} {num2} = {result}')