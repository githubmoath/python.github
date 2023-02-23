numbers=[44,50,15,70,88,54]
numbers.sort(reverse=True)
n=0
for num in numbers:
    if num %5 ==0:
        n+=1
        print(f'"{n} => {num}"')
print('All Numbers Printed')