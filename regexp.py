import re
email = input("User , Enter your Email adddress ").strip()
# if re.search(r".+@.+\.edu",email):  # r here means raw string to specidy we dont want \. literally
# if re.search(r"^[^@]+{1}@[^@]+\.edu$",email):   # [^char] should not have char
# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$",email):  others have simplifies our problem by 
if re.search(r"^\w+@(\w+\.)?\w+\.(edu|com|net|gov)$",email,re.IGNORECASE):  
# re.match where we dont need match as it start automatically starts at rigth place
# re.fullmatch where we dont need match as it automatically at all 
    # ? for 0 to 1 repetation
    # {m} for m repetation
    # {m,n} for m to n repeataton
    # d is Decimal D is not a decimal
    # w is word W is not
    #  s is whitespace S is not whitespace
    # (?:..) means ... in particular ordder is not needed
    print("Valid")
else:
    print("Invalid")

    #  ^ represents start of strong and $ represents its end