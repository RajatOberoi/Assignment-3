#count even and odd no in a list
a=[1,5,3,9,10,11,20]
print(a)
count=0
c=0
for i in a:
    if i%2==0:
        count=count+1
    else:
        c=c+1
print("even no in list =",count)
print("odd no in list =",c)
