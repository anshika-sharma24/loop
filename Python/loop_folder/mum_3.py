# harshad number
num=int(input("enter your number:"))
num1=num
sum=0
while num >0:
      num2=num%10
      sum=sum+num2
      num=num//10
if num1%sum==0:
      print("harshad number",num1)    
else:
      print("not harshad number",num1)  


 
