my_friends=[]
terms=4
while 0 < terms:
    name=input('Enter name: ').strip()
    if name.isupper():
        print('Error name!, Enter another name')
    elif name.islower():
        my_friends.append(name.capitalize)
        print(f'Friend {name.capitalize} Added to my_friend After Capital ')
    elif name.istitle:
        my_friends.append(name)
        print(f'{name} Add To my_friend')
    terms-=1
    if terms>0 :
        print(f'stay {terms} names left')
    else:
        print('my_friend is fulled')
