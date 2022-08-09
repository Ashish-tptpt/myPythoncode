import re
url = input("URL: ").strip()
# username = url.replace("https://twitter.com/","")
# username = url.removeprfix("https://twitter.com/")
# user = re.sub(r"(https?://)?(www\.)?twitter\.com/","",url)# re sub for substitute
if matches := re.search(r"^(?:https://)?(?:www\.)?twitter\.com/([a-zA-Z0-9_]+)$",url,re.IGNORECASE): # if user types somethong else
    print(f"Usename:",matches.group(1)) # (?:..) means dont capture it 