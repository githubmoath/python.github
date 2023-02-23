
with open(r'F:\Enmaa\Python\python.github\Projects_Python\Questions1.csv' , 'r') as myfile:

    w = 0
    score = 0

    ans_true = [1,2,4,3,1,2,1,4]

    for q in myfile:
        print(myfile.readline())
        ans1 = int(input("pleas enter a number from 1 to 4 >>> ").strip())
        if ans1 == ans_true[w]:
            print('"Your answer is true"')
            score += 1
        else:
            print('"Your answer is false!"')
        w += 1

    print('')
    print('your score:' + str(score) + ' from 8')
