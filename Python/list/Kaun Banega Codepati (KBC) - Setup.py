
question_list = [ "1.How many continents are there?" ,           
    "2.What is the capital of India?" ,          
    "3.NG mei kaun se course padhaya jaata hai?" 
]
life_line=[5050]
opt1=["four","bhopal","software"]
opt2=["nine","chennai","councling"]
opt3=["seven","chandigrah","upsc"]
opt4=["eight","delhi","mpsc"]
opt6=["seven","bhopal","software"]
opt7=["four","delhi","upsc"]
ans = [1,2,1]
solution=[3,4,1]
i=0                                                                                                                             
c=0
while(i<len(question_list)):
    print(question_list[i])
    print(1,opt1[i])
    print(2,opt2[i])
    print(3,opt3[i])
    print(4,opt4[i])
    print(5, life_line[0])
    user=int(input("enter any num"))
    if(solution[i]==user):
           print("congrats your answer is right")
    elif(user==5050):
        if c==0:

            print(1,opt6[i])
            print(2,opt7[i])
            user1=int(input("enter any num"))
            if(user1== ans[i]):
                print("Your answer is correct")
            else:
                print("your answer is wrong")
                break
            c=c+1
        else:
            print(" sorry you used already 50-50life_line")
    
    else:
           print("sorry your answer is wrong")
           break
    i=i+1       

       

  