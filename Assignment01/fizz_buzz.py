def fizz_buzz(num):
    if num%3==0 and num%5==0:
        return 'FizzBuzz'
    elif num%5==0:
        return 'Buzz'
    elif num%3==0:
        return 'Fizz'
    else:
        return num
num = int(input())
print(fizz_buzz(num))