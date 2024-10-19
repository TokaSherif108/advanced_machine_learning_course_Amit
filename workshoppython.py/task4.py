# lazm bigger than 3shan yt2kd 
'''def match_str(str1,str2):
    longest_str=""
    for i in range (len(str1)):
        #print(i)
        for j in range(i,len(str1)):
            sub_str = str1[i:j+1]r
            #print(sub_str)
            if sub_str in str2:
                if len(sub_str) > len(longest_str):
                    longest_str=sub_str
    return(longest_str)
str1=input(" string 1 ")
str2=input(" string 2 ")
print(match_str(str1,str2))
'''
# class
class matchstr:
    def __init__(self,str1,str2):
        self.str1=str1
        self.str2=str2
        
        
    def matstr(self):
        longstr=''
        for i in range(len(self.str1)):
            for j in range(i,len(self.str1)):
                substr=self.str1[i:j+1]
                if substr in self.str2:
                    if len(longstr)< len(substr):
                        longstr=substr
        return longstr
str1=input(" string 1 ")
str2=input(" string 2 ")
s=matchstr(str1,str2)
print(s.matstr())