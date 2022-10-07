import re
str1= input("Enter a valid email ID: ")
res=re.split(r"@",str1)
username, domain =res[0], res[1].split('.')[0]
print("Your username is {} and Domain is {}".format(username, domain))







