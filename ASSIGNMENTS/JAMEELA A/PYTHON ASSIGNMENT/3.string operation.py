
operation = int(input('''
choose an operation from the following:
1.concatenation
2.reverse
3.slicing
'''))

if operation == 1:
    string1 = input('Enter your first string: ')
    string2 = input('Enter your second string: ')
    print('concatenated string is',string1+string2)

elif operation == 2:
    string=input('Enter a string:')
    rev=string[len(string)::-1]
    print('Reversed string is',rev)

elif operation == 3:
    string=input('Enter a string:')
    index1=int(input('enter starting index:'))
    index2=int(input('enter ending index:'))
    print("Sliced string : ", string[index1:index2+1])

else:
    print('You have not typed a valid operation, please run the program again.')
