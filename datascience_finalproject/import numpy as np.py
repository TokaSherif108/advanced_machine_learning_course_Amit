import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#handle null in member_birth_year 
plt.figure(figsize=(6,2))
plt.title('member_birth_year')
plt.hist(df['member_birth_year'])
plt.show()
c=['member_birth_year']
median=dict(df[c].median())
# not-normally distributed, replace null with median
df.fillna(median,inplace=True)