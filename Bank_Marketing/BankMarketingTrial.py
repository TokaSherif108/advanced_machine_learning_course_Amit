#import libraries
import warnings
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")
#read file
df = pd.read_csv("C:/Users/toka_/Desktop/AMIT/advanced_machine_learning_course_Amit/Bank_Marketing/bank.csv")
#
df.head(5)
#drop un nessary columns
cols_to_drop = ['contact', 'day', 'month', 'duration', 'previous']
df.drop(cols_to_drop, axis=1, inplace=True)





#relationship between numerical cols and target
num_cols=df.select_dtypes("number").columns
plt.figure(figsize=(6,3))
for i,col in enumerate(num_cols):
    plt.subplot(2,2,i+1)
    sns.barplot(x="deposit",y=col,data=df)
    plt.xticks

# Pivot table like in excel     
agg = df.pivot_table(index = "deposit", columns="loan", aggfunc=len, values="marital")
display(agg)
sns.heatmap(agg, annot=True)