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

plt.plot(x,y, label='real line')
plt.plot(x,y_, label='prediction line')
plt.legend(loc=4)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Simple Linear Regression')

plt.savefig('simple_linear_regression1.png')
plt.show()
