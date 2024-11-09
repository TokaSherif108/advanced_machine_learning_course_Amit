import pandas as pd
'''s=pd.Series([1,2,3,4])
s2=pd.Series([1,2,3,4]),index=["A","B","C","D"]'''
#create data frame 
data1=[[1,444,"abc"],
    [2,555,"def"],
    [3,666,"ghi"],
    [4,44,"xyz"]]
df=pd.DataFrame(data1,columns=["col1","col2","col3"])
print (df)
#another way to create data frame
data2={"col1":[1,2,3,4],
    "col2":[444,555,666,444],
    "col3":["abc","def","ghi","xyz"]}
df2=pd.DataFrame(data2)
print(df2)
df.describe