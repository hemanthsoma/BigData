def binarySearch(numbers,low,high,search):
    if high>=low:
        mid=(low+high)//2
        if numbers[mid]>search:
            return mid
        elif numbers[mid]>search:
            return binarySearch(numbers,low,mid-1,search)
        else:
            return binarySearch(numbers,mid+1,high,search)
numbers=[1,2,3,4,5,6,7,8]
search=int(input('Enter number to search'))
result = binarySearch(numbers,0,len(numbers)-1,search)
if result!=-1:
    print('Element found at at position',result)
else:
    print('Element not found')