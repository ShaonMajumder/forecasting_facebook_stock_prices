from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

x = np.array([1,2,3,4,5,6],dtype=np.float64)
y = np.array([2,3,4,5,4,6],dtype=np.float64)

def m_b(x,y):
    m = ((mean(x)*mean(y)) - mean(x*y)) / ((mean(x)**2) - mean(x**2))
    b = mean(y)-m*mean(x)
    return m,b

m,b= m_b(x,y)
y_ = m*x + b

# prediction
prediction_x = 6.5
prediction_y = m*prediction_x + b

plt.scatter(x,y, label='real data points', color='r')
plt.scatter(prediction_x,prediction_y, label='single prediction', color='g')
plt.plot(x,y_, label='prediction line')

plt.legend(loc=4)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Simple Linear Regression(SLR)')
plt.tight_layout()
plt.savefig('simple_linear_regression1.png')
plt.show()


plt.scatter(x,y, label='real data points', color='r')
plt.plot(x,y_, label='prediction line')
i=0

for xi,y_i,yi in zip(np.nditer(x),np.nditer(y_),np.nditer(y)):    
    plt.plot([xi,xi],[y_i,yi],label='error',color='b')
    if i == 0:
        i=1
        plt.legend(['Prediction line', 'Prediction Error' , 'Data Points'],loc=4)
        
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Errors of Prediction SLR')
plt.tight_layout()
plt.savefig('errors1')
plt.show()
