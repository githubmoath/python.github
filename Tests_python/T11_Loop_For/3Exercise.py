my_ranks= {
    'Math' : 'A',
    'Science' :'B',
    'Drawing' :'A',
    'Sports' : 'C'
}

ranks = {
    'A': '100',
    'B': '80',
    'C': '40'
}
total=0

for subject,value in my_ranks.items():
        print(f'"My Rank in {subject} Is {value} And This Equal {ranks[value]} Points"')
        total+=int(ranks[value])

print(f'"Total Points Is {total}"')
