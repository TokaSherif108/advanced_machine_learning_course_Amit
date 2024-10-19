import random
'''def gen_pass(lenght):
    characters="abcdefgABCDEFG123456789@#$%^&*"
    numofchar=len(characters)
    password=''
    for i in range(lenght):
        rand_indx=random.randrange(0,numofchar)
        password += characters[rand_indx]
    return password'''

#class
class genpass:
    def __init__(self,length):
        self.length=length
    def gen_pass(self):
        characters="abcdefgABCDEFG123456789@#$%^&*"
        numofchar=len(characters)
        password=''
        for i in range(self.length):
            rand_indx=random.randrange(0,numofchar)
            password = password + characters[rand_indx]
        return password
length=int(input("lenght"))
p=genpass(length)    
print(p.gen_pass())        