'''Task-1
Suppose you have this email address “Amit_ml@gmail.edu”
- Input Validation: Check if the input string contains exactly one "@" symbol and 
at least one "." after the "@" symbol. If it's not a valid email, return "Invalid 
email".
- Extract Username: Extract and return the part of the email before the "@" 
symbol.
- Extract Domain: Extract and return the domain (the part between "@" and the 
last ".").
- Check for Domain Ending: Check if the email ends with ".com". If it does, 
return "Commercial Domain". If it ends with ".edu", return "Educational Domain". 
Otherwise, return "Other Domain".'''
email="Amit_ml@gmail.edu"
output1=email.count("@")
print(output1)
output2=email[7:]
x=output2.count(".")
if x >= 1 and output1==1:
    print("valid email")
else:
    print("invalid email")
print(email[0:7])
print(email[8:13])
print(email.endswith)