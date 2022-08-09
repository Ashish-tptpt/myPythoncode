import re

name = input("Enter your name ? ").strip()


# the data wanted(firstname)(lastaname) is in brackets

if matches:= re.search(r"^(.+), *(.+)$",name):
    # lna, fna = matches.groups() 
    name = matches.group(2)+" "+matches.group(1)

#  := is walrus operator that checks and assignes value at same time

print(f"Hello {name}")