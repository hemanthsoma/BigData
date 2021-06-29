def sumOfMultiplesOf3and5(limit):
    l = []
    i = 1
    while True:
        l.extend([3*i,5*i])
        if 3*i==limit or 5*i==limit:
            break
        i+=1
    return sum(l)
limit = int(input())
print(sumOfMultiplesOf3and5(limit))