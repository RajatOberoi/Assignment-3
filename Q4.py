#creating a list with number and sorting in ascending order
a=int(input("enter no of element in list"))
x=[]
for i in range(a):
                c=int(input("enter no"))
                x.append(c)
print(x)
#after sorting
print("after sorting")
x.sort()
print(x)
