'''Task-2:
Encoded Message:
###!!@mocleW EPGTQ!!!6789
Steps to Decode:
1. Extract the core part of the message: "mocleW EPGTQ".
2. Reverse the first word: "mocleW" becomes "Welcome".
3. Replace shifted vowels in the second word:
o "EPGTQ": No vowels to change.
4. Final decoded message: "Welcome PGTQ".'''
message="###!!@mocleW EPGTQ!!!6789"
corepart=message[6:18]
rev1word=message[-14:-20:-1]
print(message[6:18])
print(message[-14:-20:-1])
replace=message.replace("E","")
print(corepart,rev1word)