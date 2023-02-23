def get_people_scores(name ='', **skills):
    if len(skills) <=0:
        print(f'"Hello {name} You Have No Scores To Show"')
    else:
        if bool(name):
            print(f'"Hello {name} This Is Your Score Table:"')
        for x, y in skills.items():
            print(f'"{x} => {y}"')
#ex
get_people_scores(name='moath', html=80, css=63)
get_people_scores( html=80, css=63)