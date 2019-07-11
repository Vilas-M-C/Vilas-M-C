import numpy as np

import pandas as pd

data=pd.read_csv('headbrain.csv')
y=data.iloc[:,2].values
x=data.iloc[:,3].values
x_mean=np.mean(x)
y_mean=np.mean(y)

def beta_x(x,x_mean):
    bet_x=0
    bet_xsq=0
    for i in range(0,len(x)):
        bet_x+=i(i-x_mean)
        bet_xsq+=(x[i]-x.mean)**2
        return bet_x,bet_xsq
    
def beta_y(y,y_mean):
    bet_y=0
    for i in range(0,len(y)):
        bet_y+=(y[i]-y_mean)
    return bet_y
      
x_b,x_bs=beta_x(x,x_mean)
y_b=beta_y(y,y_mean)
beta1=(x_b*y_b)/x_bs