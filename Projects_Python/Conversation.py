
name= input('What is your name? ')
print(f'Hi {name} :)')
age = int(input('How old are you? '))

if age <=12:
    sp=input('What is your favourite sport? ').lower().strip()
    if sp =='football':
        print('I love football too ')
        po = input('What is your position in the game?').lower().strip()
        print("It's good")
    elif sp =='Basketball':
        print("It's a hard game")
    elif sp == 'tennis':
        print("It's enjoyable game!")
    else:
        print('Good, continue')


else:
    mr= input('Are you marred? ').lower().strip()
    if mr =='yes':
        ch =input('Do you have children? ').lower().strip()
        if ch == 'yes':
            print('The children are beautiful')
        elif ch =='no':
            print("Don't worry it will come to you")
        else:
            print('Please enter yes or no')

    elif mr=='no':
        car = input('Do you have a car? ').lower().strip()
        if car == 'yes':
            print('Wonderful')
            kind = input('What kind').lower().strip()
            if kind =='pmw' or kind =='odi':
                print('Wao!')
            else:
                print('it is a beautiful car!')


    else:
        print('Please enter yes or no')