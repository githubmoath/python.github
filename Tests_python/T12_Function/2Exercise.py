
def addition (*add):
    sum= 0
    for num in add:
        if num == 10:
            continue
        elif num == 5:
            sum -= num
        else:
            sum +=num
    print(sum)

#example
addition(4,5,6,5,6,2,10,6)