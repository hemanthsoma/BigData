def checkingSpeed(n):
    if n<70:
        return 'Ok'
    count = 0
    for _ in range(70,n,5):
        count+=1
    if count > 12:
        return 'License Suspended'
    else:
        return f'Points {count}'
n=int(input())
print(checkingSpeed(n))