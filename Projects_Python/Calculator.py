# import tkinter as tk

# window= tk.Tk()
# window.title('Calculator')


# lpl=tk.Button(window,text='+')
# lpl=tk.Grid()
# lpl.pack()

# window.geometry('400x400')
# in1=tk.Entry(width=20, )
# in1.pack()

########################-------------------------------------

num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))
op = input('Enter your calculation: ')
result=''

if op =='+':
    result=num1+num2
elif op == '-':
    result=num1-num2
elif op == '*':
    result=num1*num2
elif op == '/':
    result=num1 / num2
else:
    print( 'Please enter another value ')

print(result)