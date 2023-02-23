students = {
    'Ahmad':{
        'Math' : 'A',
    'Science' :'D',
    'Drawing' :'B',
    'Sports' : 'C',
    'Thinking':'A'
    },
    'Moath':{
        'Math' : 'B',
    'Science' :'B',
    'Drawing' :'B',
    'Sports' : 'D',
    'Thinking':'A'
    },
    'Omar':{
        'Math' : 'D',
    'Science' :'A',
    'Drawing' :'A',
    'Sports' : 'B',
    'Thinking':'B'
    }
}

ranks = {
    'A': '100',
    'B': '80',
    'C': '40',
    'D': '20'
}

for name, data in students.items():
    print('"__________________"')
    print(f'"__Student Name => {name}" ')
    print('__________________')
    total = 0
    for subject,marks in data.items():
        print(f'"_{marks} => {ranks[marks]} Points"')
        total+=int(ranks[marks])
    print(f'"Total Points For {name} is {total}"')