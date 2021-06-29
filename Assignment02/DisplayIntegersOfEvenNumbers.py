for i in range(100,200):
    sum=0
    while i!=0:
        digit=i%10
        sum+=digit
        i//=10
    if sum%2==0:
        print(i)