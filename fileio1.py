# file=open("Names.txt","w") write overwrites all
# with open("Names.txt","a") as file:
#     for _ in range(3):
#         name = input("What is your name?")
#         file.write(f"{name}\n")
# file.close() No need if use with
from unicodedata import name


names =  []
with open("Names.txt","r") as filer:
#     nline= filer.readlines()
# for x in sorted(nline):
#     print(x.rstrip())
    for line in filer:
        names.append(line.rstrip())
    
for x in sorted(names,reverse=True):
    print(x)



