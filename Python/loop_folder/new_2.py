# armstrong number
num=int(input("enter your number"))
num1=num
sum=0
while num>0:
    num2=num%10
    sum=sum+num2**3
    num=num//10
if sum==num1:
    print(num1,"armstrong")
else:
    print(num1,"not armstrong")