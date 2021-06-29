count = int(input())
List = float(map(int,input().split()))
product=1
for i in List:
    product*=i
print('Total product is ',product)