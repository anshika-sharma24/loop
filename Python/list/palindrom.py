
name=input("enter----")
i=0
s=""
while i<len(name):
    i=i+1
    s=s+name[-i]
if name==s:
    print("it is palidrom")
else:
    print("it is not--")
    