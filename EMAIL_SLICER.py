import regex
str1= input("Enter a valid email ID: ")
pattern='^[a-zAA-Z0-9-_]+@[a-zA-Z0-9]+.[a-zA-Z]{1,3}$'
if re.match(pattern, str1):
    res=re.split(r"@",str1)
    username, domain =res[0], res[1].split('.')[0]
    print("Your username is {} and Domain is {}".format(username, domain))
else:
    print("Enter a valid email ID")




        

