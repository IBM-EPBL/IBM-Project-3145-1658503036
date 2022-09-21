operation = int(input('''
choose an operation :
1.concatenation
2.reverse
3.slicing
'''))

if operation == 1:
    str1 = input('Enter your first string: ')
    str2 = input('Enter your second string: ')
    print('concatenated string is',str1+str2)

elif operation == 2:
    str=input('Enter a string:')
    rev=str[len(str)::-1]
    print('Reversed string is',rev)

elif operation == 3:
    string=input('Enter a string:')
    ind1=int(input('enter starting index:'))
    ind2=int(input('enter ending index:'))
    print("Sliced string : ", string[ind1:ind2+1])

else:
    print('You have not typed a valid operation, please run the program again.')