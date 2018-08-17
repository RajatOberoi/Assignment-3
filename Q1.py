#creating list with user defined input
x=[]
y=int(input("enter how many element you want in list"))
for i in range(y):
    a=int(input("enter 1 for number,enter 2 for string"))
    if a==1:
            c=int(input("enter number"))
            x.append(c)
    elif a==2:
            v=input("enter string")
            x.append(v)
    else :
            print("enter a valid choice")
            break
print(x)          
