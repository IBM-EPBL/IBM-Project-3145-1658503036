
print(" 1.Add \n 2.Subtract \n 3.Multiply \n 4.Divide \n 5.END")

while(True):
    op=int(input("choose operation from above : "))

    if op==1:
        n1=int(input("Enter number 1: "))
        n2=int(input("Enter number 2: "))
        print(n1,"+",n2,"=",n1+n2)

    elif op==2:
        n1=int(input("Enter number 1: "))
        n2=int(input("Enter number 2: "))
        print(n1,"-",n2,"=",n1-n2)

    elif op==3:
        n1=int(input("Enter number 1: "))
        n2=int(input("Enter number 2: "))
        print(n1,"*",n2,"=",n1*n2)

    elif op==4:
        n1=int(input("Enter dividend: "))
        n2=int(input("Enter divisor: "))
        print(n1,"/",n2,"=",n1/n2)

    elif op==5:
        break;

    else:
        print("invalid output")

    
