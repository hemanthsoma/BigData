count = int(input())
List = list(map(int,input().split()))
sum = 0
for i in List:
    sum+=i
print(sum/count)
