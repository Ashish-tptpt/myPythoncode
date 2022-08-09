import csv

students=[]

# with open("names.csv","r") as file:
#     for line in file:
#         name ,home = line.rstrip().split(",")
#         students.append({"name":name,"house":home})
                # def housed(x):
                    #     return(x["house"])

                    # # for x in sorted(students,key=housed):


with open("names.csv","r") as file:
    reader = csv.reader(file)
    for name ,row in reader:
        students.append({"name":name,"house":row})

for x in sorted(students,key=lambda student: student["house"]):
    print(x["house"])