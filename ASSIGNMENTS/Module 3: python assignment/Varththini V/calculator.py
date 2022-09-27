n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))

op=input('''
choose the operation to be done:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

if op=='+':
    print("After addition:", n1+n2)

elif op=='-':
    if n1>n2:
        print("After subtraction:", n1-n2)
    else:
        print("After subtraction:", n2-n1)

elif op=='*':
    print("Aftermultiplication:", n*n2)

elif(op=='/'):
    print("After division:", n1/n2)

else:
    print("Please,check your input operation!!")
