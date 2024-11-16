''' pd.set_option('display.max_columns', None) 
l ezhar kol columns '''
# bdwr 3la s3r el bet 
# 
import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from warnings import filterwarnings

filterwarnings("ignore")
pd.set_option('display.max_columns', None)
df = pd.read_csv("Houses.csv")
display(df.head(2))
print(df.shape)
df.drop(["Id"], axis=1, inplace=True)
pd.DataFrame({"Dtypes": df.dtypes, "Num_Uniq": df.nunique()}).T

