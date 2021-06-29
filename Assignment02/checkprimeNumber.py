number=int(input())
flag=0
for i in range(2,number):
    if number%i==0:
        flag=1
        break
if flag==0:
    print(number,'is a prime Number')
else:
    print(number,'is not a prime Number')