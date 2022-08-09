import sys
while True:
    email = input("User , Enter your Email adddress ").strip()
    username ,domain = email.split("@")
    # if username and "." in domain:
    if username and domain.endswith(".edu"):
        print("Valid")
        sys.exit()
    else:
        print("Invalid") 
        