from math import sqrt
first=float(input('Enter first coefficient'))
second=float(input('Enter second coefficient'))
third=float(input('Enter third coefficient'))
if first!=0.0:
    d=(second*second)-(4*first*third)
    if d==0.0:
        print('The roots are real and equal.')
        r=-second/(2*first)
        print('The roots are ',r,'and',r)
    elif d>0.0:
        print('The roots are real and distinct')
        r1=(-second+(sqrt(d))/(2*first))
        r2=(-second-(sqrt(d))/(2*first))
        print('The root1 is: ',r1)
        print('The root2 is: ',r2)
    else:
        print('The roots are imaginary')
        rp=-second/(2*first)
        ip=sqrt(-d)/(2*first)
        print('The root1 is ',rp,'+ i',ip)
        print('The root2 is ',rp,'+ i',ip)
else:
    print('Not a quadratic Equation')
        