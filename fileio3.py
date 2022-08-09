import csv

students=[]

#here we use dictionaries in csv, 

with open("names.csv","r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name":row["name"],"house":row["house"]})
        # When we put hin -->  put in name , house   
        #we can interchange rows but with csv.DictReader it doesnt matter 

for x in sorted(students,key=lambda student: student["house"]):
    print(x["house"])