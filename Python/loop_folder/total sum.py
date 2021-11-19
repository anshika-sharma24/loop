list1=[[1,2,3],[4,5,6],[7,8,9]]
new=[]
i=0
sum=0
while i<len(list1)-1:
    j=0
    while j<len(list1[i]):
        k=0
        while k<len(list1[i])-3:
            sum=(list1[i][0]+list1[i+1][j]+list1[i+2][k])
            new.append(sum)
            k+=1
        j+=1
    i+=1
print(sum)