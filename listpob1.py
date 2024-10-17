#swaping in list
n=int(input("enter the size of list:"))
list=[]
for _ in range(n):
    num=int(input())
    list.append(num)
idx1=int(input("enter the index1 number:"))
idx2=int(input("enter the index2 number:"))
temp=list[idx1]
list[idx1]=list[idx2]
list[idx2]=temp
print(list)
