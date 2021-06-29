def isPalindrome(string):
    if string==string[::-1]:
        return True
    return False
string = input()
result = isPalindrome(string)
if result==1:
    print('The string is palindrome')
else:
    print('The string is not palindrome')