friends=['Osama', 'Ahmed', 'Sayed', 'Ali' , 'jaky','Mahmoud']
for x in friends:
    if len(x) %2==1:
        print(f'"{x}",',end=' ')
print('')
for x in friends:
    if len(x) %2==0:
        print(f'"{x}",',end=' ')