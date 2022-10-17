n=int(input("Enter the number of elements : "))

list=[]
for i in range(0,n):
    element=int(input())
    list.append(element)
    
    
print('\n')
num=int(input("Enter the integer to be inserted in the array:"))
ind=int(input("Enter the index:"))
list.insert(ind,num)
print("After inserting: ")
print(list)

print('\n')
num=int(input("Enter the integer to be removed:"))
list.remove(num)
print("After removing: ")
print(list)

print('\n')
num=int(input("Enter the integer to be inserted in the list :"))
ind=int(input("Enter the index :"))
list.insert(ind,num)
print("After inserting : ")
print(list)

print('\n')
list.sort();
print("After sorting : ")
print(list)


print('\n')
list.pop();
print("After popping:")
print(ls)

print('\n')
list.reverse()
print(ls)