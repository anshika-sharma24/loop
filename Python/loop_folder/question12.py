

i=1
sum=0
while(i<=11):
    user=int(input("enter your number"))
    sum=sum+user
    i=i+1
average=sum/user
print(average)
if average/5==0:
    print("divisble")
else:
    print("not divisble")
