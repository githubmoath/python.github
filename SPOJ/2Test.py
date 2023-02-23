N= int(input('Please enter hte positive integer N:'))

my_list =[]

if N ==0:
    print(f'{N} must be greater than 0!')
else:
    print(f'The number-triangle that has {N} lines is:')
    for x in range(1,N+1):
        z=''
        for y in range(1,x+1):
            z+=str(y)+' '
        my_list.append(z)

for i in my_list:
    print(i)