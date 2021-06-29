count=int(input())
product=1
for i in range(count):
    number=float(input())
    product*=number
GeometricMean = pow(product,1.0/count)
print('The Geometric Mean is: ',GeometricMean)