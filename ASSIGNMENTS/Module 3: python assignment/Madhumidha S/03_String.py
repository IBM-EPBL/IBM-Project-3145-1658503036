print("String operations\n1.concatenate\n2.reverse\n3.slice")


op=int(input("Choose an operation from above : "))

if op==1:
    s1=input("Enter first string: ")
    s2=input("Enter second string: ")
    print(s1+s2)

if op==2:
    s=input("Enter the string:")
    r=s[len(s)::-1]
    print("Reversed String : ",r)

if op==3:
    s=input("Enter the string:")
    start=int(input("Enter starting index: "))
    end=int(input("Enter end index: "))
    print("Sliced string : ", s[start:end+1])

