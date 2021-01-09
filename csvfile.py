import csv
with open("emp.csv","w",newline='') as f:
    w=csv.writer(f)
    w.writerow(["ID","NAME","SAL"])
    empid =input("enter your employee id")
    ename=input("enter your name")
    esal=input("enter your salary")
    w.writerow([empid,ename,esal])
    ename=input("enter your name")
    esal=input("enter your salary")
    w.writerow([ename,esal])
    empid=input("enter your employee id")
    ename=input("enter your name")
    w.writerow([empid,ename])
    empid=input("enter your employee id")
    ename=input("enter your name")
    w.writerow([empid,ename])
    empid =input("enter your employee id")
    ename=input("enter your name")
    esal=input("enter your salary")
    w.writerow([empid,ename,esal])

    