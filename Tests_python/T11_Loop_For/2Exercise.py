for x in range(1,21):
    if x in [6,8,12]:
        continue
    elif x <10:
        print(f'"0{x}"')
    else:
        print(f'"{x}"')
print('All Number Printed')