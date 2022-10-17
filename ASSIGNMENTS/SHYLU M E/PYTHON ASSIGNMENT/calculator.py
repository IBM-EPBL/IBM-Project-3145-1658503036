operation = input('''
choose an operand:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

num1 = int(input('''Enter your first number: '''))
num2 = int(input('Enter your second number: '))

if operation == '+':
    print("Addition:" ,num1+num2)

elif operation == '-':
    print("subtraction :" ,num1-num)

elif operation == '*':
    print("multiplication :",num1*num2)

elif operation == '/':
    print("Division :",num1 / num2)

else:
    print('You have not typed a valid operator, please run the program again.')