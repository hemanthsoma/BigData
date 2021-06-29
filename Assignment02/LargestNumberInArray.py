numbers=[1,2,3,4,5,6,7,8]
maxi = numbers[0]
position=0
for i in range(len(numbers)):
    if maxi<numbers[i]:
        maxi=numbers[i]
        position=i
print('Largest Number is',maxi,'at positon',numbers.index(maxi))