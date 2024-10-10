email=input("enter email")
at=email.count("@")
atnumber=email.find("@")
dot=email[atnumber:].count(".")
dotposition=email[-1:].find(".")
domain=email[atnumber:dotposition]
if at==1 and dot > 0:
    print("valid email")
    print ('username is :',email[0:atnumber])
    print("domain is:",domain)
    if email[dotposition:] == ".com":
        print("commercial")
    elif email[dotposition:] ==".edu":
        print("education")
    else:
        print("other")
else:
    print("invalid email")
    