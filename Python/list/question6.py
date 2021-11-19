list=[1,2,-1,0,3,0,4,5,0,0,0]
i=0
b=[]
c=[]
d=[]
count=0
while i<len(list):
    if list[i]==0:
        b.append(list[i])
        count+=1
    elif list[i]== -1   :
         d.append(list[i])
    else:
        c.append(list[i])
    i+=1

print(c+b+d)
print(count)




