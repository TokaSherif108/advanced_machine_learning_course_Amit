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
#rsmt el model w b3dha ha5od b2a coeff w intercept 
my_model=LinearRegression()
my_model.fit(x_train,y_train)
plt.scatter(x_train, y_train, color = 'red')
plt.scatter(x_test, y_test, color='green', label='Test data')
plt.plot(x_train, my_model.predict(x_train), color = 'blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
y_pred = my_model.predict(x_test)
c = [i for i in range(1,len(y_test)+1)]
plt.plot(c,y_test,color='r',linestyle='-')
plt.plot(c,y_pred,color='b',linestyle='-')
plt.xlabel('Salary')
plt.ylabel('index')
plt.title('Prediction')
plt.show()
print('Intercept of the model:',my_model.intercept_)
print('Coefficient of the line:',my_model.coef_)