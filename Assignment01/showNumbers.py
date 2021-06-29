def showNumbers(limit):
    for i in range(limit+1):
        if i%2==0:
            print(f'{i} EVEN')
        else:
            print(f'{i} ODD')
limit = int(input())
showNumbers(limit)