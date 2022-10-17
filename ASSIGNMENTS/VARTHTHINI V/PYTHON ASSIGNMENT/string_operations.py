op=input('''
choose the operation to be done:
a for concatenation
b for reverse
c for slicing
''')

if(op=='a'):
    s1=input("Enter first string:")
    s2=input("Enter second string:")
    print("After concatenation the string is ",s1+s2)

elif(op=='b'):
    s1=input("Enter the string:")
    r=s1[len(s1)::-1]
    print("The reversed string is ",r)

elif(op=='c'):
    s1=input("Enter the string:")
    st_inx=int(nput("Enter starting index:"))
    ed_inx=int(nput("Enter ending index:"))
    print("After slicing of the string:", s1[st_inx:ed_inx+1])

else:
    print("You have given invalid operation")
