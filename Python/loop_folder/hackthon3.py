num=int(input("enter your number"))                                                                                                 
i=1
counter=0
while (i<=12):
    if (num%i == 0):
        counter=counter+1
    i=i+1
if counter==2:
        print(num,"prime n")
else:
        print(num, "not prime number")
