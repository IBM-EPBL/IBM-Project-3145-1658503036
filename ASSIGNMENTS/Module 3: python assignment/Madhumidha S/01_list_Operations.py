list=[]
print("1.insert\n2.remove\n3.append\n4.sort\n5.pop\n6.reverse\n7.END")

while(True):
    op=int(input("Enter the number corresponding to operations given above: "))
    if op==1:
        pos=int(input("enter the position: "))
        num=int(input("enter the number : "))
        list.insert(pos,num)
        print(list)
        
    elif op==2:
        num=int(input("enter the number to remove : "))
        list.remove(num)
        print(list)
        
    elif op==3:
        num=int(input("enter the number to append : "))
        list.append(num)
        print(list)
    
    elif op==4:
        list.sort()
        print("list : " , list)
    
    elif op==5:
        print("popped : ",list.pop())
        print(list)
    
    elif op==6:
        list.sort(reverse=True)
        print(list)
        
    elif(op==7):
        break;
    
    else:
        print("invalid input")


print("Final list  = ",list)

