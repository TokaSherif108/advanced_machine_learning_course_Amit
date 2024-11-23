import pandas as pd
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_squared_error
import warnings
warnings.filterwarnings('ignore')
data=pd.read_csv(r"C:/Users/toka_/Desktop/AMIT/advanced_machine_learning_course_Amit/Linear_regression_session1/Salary_Data.csv")
data.tail()
data.info()
data.describe()
plt.figure(figsize=(3,3))
sns.pairplot(data,x_vars=["YearsExperience"],y_vars=["Salary"],size=7,kind="scatter")
plt.xlabel("years")
plt.ylabel("salary")
plt.title("salary prediction")
plt.show()
#cooking the data
x=data.iloc[:,:-1]
y=data.iloc[:,1]
#random state bsbtha 3shan kol mara b2sm data ya5od nfs 7aga k train w k test 
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.8,random_state=10)
