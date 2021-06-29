def tillZero(number):
    if number<1:
        exit()
    else:
        print(number)
        return tillZero(number-1)
number=int(input())
print(tillZero(number))