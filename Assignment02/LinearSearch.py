List=[1,2,3,4,5,6,7,8]
flag=0
search=int(input('Enter num to search'))
for i in range(len(List)):
    if List[i]==search:
        print('Element is found')
        flag=1
        break
if flag==0:
    print('Element is not found')