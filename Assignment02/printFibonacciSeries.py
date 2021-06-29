first,second=0,1
number=int(input('Enter number of terms'))
print(first,second,end=' ')
while(number-2):
    total=first+second
    first,second=second,total
    print(total,end=' ')
    number-=1