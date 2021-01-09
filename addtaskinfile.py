f=open("mytasks.txt","a")
while True:
    print("***** My To Do App *****")
    print("1.Add Task:")
    print("2.View All Tasks:")

    
    Choose_Option=int(input("enter your option"))
    if Choose_Option==1: 
        f=open("mytasks.txt","a")
        A=input("enter your task")
        f.write(A)
        print("opration completed")
        f.close()
    elif Choose_Option==2:
        f=open("mytasks.txt","r")
        data=f.read()
        print(data)
        f.close()
    elif Choose_Option==0:
        print("Bye")
    else:
        print("you entered invalid option")

