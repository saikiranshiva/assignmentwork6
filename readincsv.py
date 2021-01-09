import csv
f=open("emp.csv","r")
data=csv.reader(f)
for i in data:
    print(i)

