friends=('Osama', 'moath', 'Omar')
x = list(friends)
x[0]='Elzero'
friends = tuple(x)
print(friends)
print(type(friends))
print(len(friends))