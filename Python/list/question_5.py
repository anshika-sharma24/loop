a=[50,40,23,70,56,12,5,10,7]
i=0
max=0
sec=0
while i<len(a):
    if a[i]>max:
        max=a[i]
    i=i+1
j=0
while j<len(a):
    if max>a[j] and a[j]>sec:
       sec=a[j]
    j=j+1
print(max) 
print(sec) 