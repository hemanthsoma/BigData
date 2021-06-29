def operations(first_operand,second_operand,operator):
    if operator=='+':
        print(first_operand+second_operand)
    elif operator=='-':
        print(first_operand-second_operand)
    elif operator=='*':
        print(first_operand*second_operand)
    elif operator=='/':
        print(first_operand/second_operand)
    else:
        print('Invalid Entry')
first_operand=int(input())
second_operand=int(input())
operator=input()
operations(first_operand,second_operand,operator)