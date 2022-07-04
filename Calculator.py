x = int(input('Enter first number: '))
y = int(input('Enter second number: '))
op = input('Enter operator: (+, -, *, /) ')

if op == '+':
    print('\nThe sum: ', x + y)
elif op == '-':
    print('\nThe defference: ', x - y)
elif op == '*':
    print('\nThe product: ', x * y)
elif op == '/':
    print('\nThe quotient: ', x / y)
else:
    print('\nInvalid operator')
