friends=['Osama', 'Ahmed', 'kmal', 'Sayed', 'ali' ,'mahmoud']
capital =0
small = 0
while capital < len(friends):
    if friends[capital].istitle():
        print(friends[capital])
    else:
        small+=1
    capital+=1
else:
    print(f'"Friends Printed And Ignored Names Count Is {small}"')



