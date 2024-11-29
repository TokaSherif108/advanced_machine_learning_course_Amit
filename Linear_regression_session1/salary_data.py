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
from sklearn.preprocessing import PolynomialFeatures
poly= PolynomialFeatures(degree=15)
x_poly_train=poly.fit_transform(x_train)
x_poly_test=poly.transform(x_test)
poly_model=LinearRegression()
poly_model.fit(x_poly_train,y_train)
y_poly_pred_train=poly_model.predict(x_poly_train)
y_poly_pred_test=poly_model.predict(x_poly_test)
x_range=np.linspace(x.min(),x.max(),100).reshape(-1,1)
x_range_poly=poly.transform(x_range)
y_range_pred = poly_model.predict(x_range_poly)
plt.scatter(x_train, y_train, color='red', label='Training data')
plt.scatter(x_test, y_test, color='green', label='Test data')
plt.plot(x_range, y_range_pred, color='blue', label='Polynomial Regression')
plt.title('Salary vs Experience')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.legend()
plt.show()

import numpy as np

# Sample data (replace with your actual data)
X = np.array([1, 2, 3, 4, 5])
y = np.array([1, 3, 2, 5, 4])

# Add a column of ones to X to account for the intercept term
X_b = np.c_[np.ones((X.shape[0], 1)), X]  # Add a column of ones to X

# Compute the parameters using the normal equation
theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

# Print the parameters
theta_0, theta_1 = theta_best
print(f"Optimized parameters: theta_0 = {theta_0}, theta_1 = {theta_1}")

# Make predictions using the optimized parameters
y_pred = X_b.dot(theta_best)

# Plotting the data points and the regression line
import matplotlib.pyplot as plt

plt.scatter(X, y, color='blue', label='Data Points')
plt.plot(X, y_pred, color='red', label='Regression Line')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression Fit using Normal Equation')
plt.legend()
plt.show()