#creating list with user defined input
x=[]
y=int(input("enter how many element you want in list"))
for i in range(y):
    a=int(input("enter no"))
    x.append(a)
print(x)        
#counting no of times object occour in list
for i in x:
    print(i,"count =",x.count(i))
