#用于观察数据的分布特征，以找到合适的特征量
import matplotlib.pyplot as plt
import pandas as pd
import os

path = 'C:/Users/1/Desktop/start/train/data_fault_B'
#比如观察这个B类型故障的数据分布
df = df.iloc[:,0]
#用于显示DEtime,FEtime,BAtime等参数

#设置画布大小
plt.figure(figsize=(15,6))
#将6个传感器以叠加的形式呈现在画布上一起观察
for i in range(0,6):
    plt.plot(df)
plt.show()
