
marks= {
    'math': 90,
    'science': 80,
    'language':70
}

def get_people_scores(name ='', **skills):
    if len(skills) <=0:
        print(f'"Hello {name} You Have No Scores To Show"')
    else:
        if bool(name):
            print(f'"Hello {name} This Is Your Score Table:"')
        for x, y in skills.items():
            print(f'"{x} => {y}"')
