from math import sqrt
a = float(input("Enter length of side a: "))
b = float(input("Enter length of side b: "))
c = float(input("Enter length of side c: "))
s = (a+b+c)/2
area = sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of Triangle is :",area)