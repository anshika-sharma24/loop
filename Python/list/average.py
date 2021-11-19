elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
sum=0
sum1=0
average=0
average1=0
count=0
count1=0

while i<len(elements):
    if (elements[i])%2==0:
        count=count+1
        sum=sum+elements[i]
        average=sum//count


    else:
        count1=count1+1
        sum1=sum1+elements[i]
        average1=sum1//count1
    i=i+1
print(average)
print(average1)