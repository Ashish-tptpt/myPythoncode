import csv
name = input("Enter your name ") 
home = input("Enter Your home ")
with open("name2.csv","a") as file:
    writer = csv.writer(file)
    writer.writerow([name,home])
