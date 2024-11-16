''' pd.set_option('display.max_columns', None) 
l ezhar kol columns '''
# bdwr 3la s3r el bet 
# 
import pandas as pd 
df = pd.read_csv("Houses.csv")
df_uniques = []
for i in df.columns: 
    df_uniques.append((column, df["MiscFeature"].unique().tolist()))

df_uniques

df_uniques = {}
for i in df.columns: 
    df_uniques[i] = df[i].unique()
df_uniques