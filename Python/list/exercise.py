# # Remove duplicates from a list.
# # List = [1,2,3,1,2,2]
# # # Output: [1,2,3]
# # b=[]
# # i=0
# # while i<len(List):
# #     if List[i] not in b:
# #        b.append(List[i])
# #     i=i+1
# # print(b)



# # Our task is to print the element which occurs 3 consecutive times in a Python list.
# # Example:
# # Input: [4, 5, 5, 5, 3, 8]
# # Output: 5
# # Input: [1, 1, 1, 64, 23, 64, 22, 22, 22]
# # Output: 1, 22

# # # a=[[1,2,3,],[4,5,6,]]
# # # i=0
# # # new=[]
# # # whie i<len (a):
# # #     j=0
# # #     while j<len (a[i]):
# # #         if i==0:
# # #             sum=sum+a[i][j]
# # #         elif i==1 :
# # #             mul=mul*a[i][j]
# # #         j+=1
# # #     i+=1
# # # print(sum)
# # # print(mul)
# # # name=["a","b","c","d"]
# # # Rollno=[4,3,2,1]
# # # i=0
# # # while i<len(name):
# # #     # j=0
# # #     # while j<len(Rollno):
# # #         print(name[i])
# # #     # j=j+1
# # # i=i+1
# # # name=["a","b","c","d"]
# # # rollno=[4,3,2,1]
# # # i=0
# # # while i<len(name):
# # #     print(name[i],rollno[-i-1])
# # #     i=i+1

a=[[2,4,6,8],4,[9,2,3,7,10],11]
i=0
sum=0
sum1=0
count=0
count1=0
while i<len(a):
    j=0 
    while j<len(a[i]):
      if a[i]%2==0:
        count=count+1
        sum=sum+a[i][j]
      else:
        count1=count1+1
        sum1=sum1+a[i][j]
        j=j+1   
    i=i+1
    print(count,"even",sum)
    print(count1,"odd",sum1)







# list1=[[8,10,9],[2,5,4],[11,20,21]]
# i=0
# while i<len(list1):
#     j=0
#     max=0
#     while j<len(list1[i]):
#         if list1[i][j]>max:
#             max=list1[i][j]
#         j=j+1
#     print(max)
#     i=i+1