num= int(input('your num: '))
total=0
if num <=0:
    print('enter another num')
else:
    while num>1:
        num-=1
        if 6==num:
            continue
        else:
            print (num)
        total+=1
print(f'{total} numbers printed')

