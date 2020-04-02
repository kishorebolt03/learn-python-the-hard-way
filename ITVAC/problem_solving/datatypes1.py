#oops
print("*************\nWelcome to Python Quiz*************")
st=int(input("Enter 1 to start quiz"))
if start==1:
    Q=["Author of Python", "Which function is used to display a user content" , "Which funtion is used to get data from user"]
    O=[["GVR" , "Steve Jobs" , "J G" , "P N"] , ["print()" , "input()" , "format()" , "eval()" ] , ["print()" , "input()" , "format()" , "eval()" ]]
    A=[O[0][0] , O[1][0] , O[2][1]]
    M=[0,0,0]
    i=0
    while i<3:
        print("Your Question Q{}".format(i+1))
        print("Description {}".format(Q[i]))
        print("Options {}".format(O[i]))
        answer=input("typer your answer")
        if (answer==A[i]):
            M[i]=1
        else:
            M[i]=0
        nt=int(input("Select your options\n1.Next\n2.Previous"))
        if nt==1:
            i+=1
        elif i>0:
            i-+1
    print("Your score" ,sum(M),"out of 3")
    
