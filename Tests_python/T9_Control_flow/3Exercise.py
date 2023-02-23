age = int(input('Enter your age: '))

months= age * 12
week= months *4
day= age* 365
hour= day *24
minute= hour *60
second= minute *60

if age > 100 or age < 10:
    print('Age is nut available: ')
else:
    print(f'Your age in months is {months}')
    print(f'Your age in weeks is {week}')
    print(f'Your age in days is {day}')
    print(f'Your age in hours is {hour}')
    print(f'Your age in minutes is {minute}')
    print(f'Your age in seconds is {second}')