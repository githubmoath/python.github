N= int(input('Please enter hte positive integer N:'))

my_list =[]

if N >0 and N<=100:
    print(f'The number triangular that has {N} rows is:')
    for x in range(1,N+1):
        z=''
        for y in range(x,0,-1):
            z+=str(y)+' '
        my_list.append(z)


for i in my_list:
    print(i)

