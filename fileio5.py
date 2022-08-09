import csv

name = input("Enter Your name")
home = input("Enter Your home")

with open("name3.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name","home"])
    writer.writerow({"name": name,"home": home})