

def my_skills(name,*sk):
    if len(sk) <= 0:
        print(f' Hello {name} you have not any skill!')
    else:
        print(f'Hello {name} your skills: ')
        for s in sk:
            print(f'"_{s}"')

#example
my_skills('Moath','python', 'html', 'c++')

#ex
my_skills('omar')