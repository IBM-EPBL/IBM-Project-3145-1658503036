
operation = input('''
choose an operands from the following:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

number_1 = int(input('''Enter your first number: '''))
number_2 = int(input('Enter your second number: '))

if operation == '+':
    print(number_1,'+',number_2,'=',number_1 + number_2)

elif operation == '-':
    print(number_1,'-',number_2,'=',number_1 - number_2)

elif operation == '*':
    print(number_1,'*',number_2,'=',number_1 * number_2)

elif operation == '/':
    print(number_1,'/',number_2,'=',number_1 / number_2)

else:
    print('You have not typed a valid operator, please run the program again.')
