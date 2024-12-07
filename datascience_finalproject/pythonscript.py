import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('C:/Users/toka_/Desktop/AMIT/advanced_machine_learning_course_Amit/datascience_finalproject/datasciencefinalpowerbi.csv')
plt.figure(figsize = (10,5))
plot = sns.countplot(data=df , x='user_type',palette=['blue', 'pink'])
plt.xlabel('User distribution')
plt.ylabel('Frequency')
plt.title("Represent the user's distribution depending on being a part of the Trips Program")
plt.show()
