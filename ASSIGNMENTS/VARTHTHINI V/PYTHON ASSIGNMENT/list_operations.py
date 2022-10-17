n=int(input("Enter no. of elements in the list:"))
list=[]
for i in range(0,n):
    val=int(input("Enter value:"))
    list.append(val)

print('\n')
n1=int(input("Enter the value to be inserted in the list:"))
pos=int(input("Enter the index to be inserted:"))
list.insert(pos,n1)
print("list after insertion:",list)

print('\n')
n1=int(input("Enter the value to be removed from the list:"))
list.remove(n1)
print("list after removing:",list)

print('\n')
list.sort()
print("list after sorting:",list)

print('\n')
list.pop()
print("list after popping:",list)

print('\n')
list.reverse()
print("list after reversing:",list)

