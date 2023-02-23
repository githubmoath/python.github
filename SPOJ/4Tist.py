t = int(input('t='))

if t <= 1000 and t >0:
    for x in range(t):
        n=int(input('n='))
        if n >0 and n <=1000000:
            for y in range(1,n+1):
                print(y,end=' ')
            print('\n')