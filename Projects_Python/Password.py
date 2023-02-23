from random import choice

ex1 = "abcdefghijklmnopqrstuvwxyz"
ex2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ex3 = "0123456789"
ex4 = "!£$%/*-?^&*"
ex5 = 'abcdefghKLMNOPQRSTU89!£$%/*-?VWXYZ01234ijklmnopqrstuvwxyzABCDEFGHIJ56789!£$%/*-?.^&'

options = '''
options of password:
1 lower char
2 upper char
3 numbers
4 symbols
5 mix
'''

print(options)
kind_pass = int(input('>>> ').strip())


def pas(num):
    pass_word =''
    if kind_pass ==1:
        for x1 in range(num):
            pass_word += choice(ex1)
    elif kind_pass ==2:
        for x2 in range(num):
            pass_word += choice(ex2)
    elif kind_pass ==3:
        for x3 in range(num):
            pass_word += choice(ex3)
    elif kind_pass ==4:
        for x4 in range(num):
            pass_word += choice(ex4)
    elif kind_pass ==5:
        for x5 in range(num):
            pass_word += choice(ex5)
    else:
        print('choose from 1 -> 5 pleas')

    return(pass_word)   


print(pas(num = int(input('Enter the long of password: ').strip)))

