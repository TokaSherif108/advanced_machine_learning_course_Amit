import numpy as np
import matplotlib.pyplot as plt
# sample data(replace with your actual data )
x=np.array([1,2,3,4])
y=np.array([2,2.8,3.6,4.5])
# Initialize parameters
b=0
w=0
alpha=0.01
num_iterations=20 #( ana lama la2et el line sbt msh m7taga 1000 aw 200 kfaya 20 hwa b3dha msh ader y7sn )
#store the SSE values for plotting 
# SSE is sum square error 
sse_values=[]
#gradient descent
for i in range (num_iterations):
    #compute predictions
    y_pred=(w*x)+b
    #compute gradients
    d_b=-2*np.sum(y-y_pred)
    d_w=-2*np.sum((y-y_pred)*x)
    #update parameters
    w -= alpha*d_w
    b -= alpha*d_b
    #compute SSE and store it
    sse=np.sum((y-y_pred)**2)
    sse_values.append(sse)
    #debug : print the SSE every 100 iterations
    if (i+1)%100 == 0:
        print(f" Iteration {i+1} , SSE: {sse} ")
#print b and w in the third iteration 
    if (i==3):
        print(f" in the third iteration w= {w} and b= {b} ")
ypredict=w*5+b
print(ypredict)        
# 
# plotting the SSE values to show convergence 
plt.figure(figsize=(12,5))
# SSE over iterations 
plt.subplot(1,2,1)
plt.plot(range(num_iterations),sse_values,label="SSE")
plt.xlabel("Iteration")
plt.ylabel('SSE')
plt.title('SSW OVER ITERATION ')
plt.legend()
plt.tight_layout()
plt.show()
print(f"optimized parameters : w = {w} , b = {b} ")

