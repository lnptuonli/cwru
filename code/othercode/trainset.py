#训练数据数据整合
import pandas as pd
import numpy as np

df1 = pd.read_csv('C:/Users/1/Desktop/start/train/B01.csv')
df2 = pd.read_csv('C:/Users/1/Desktop/start/train/B02.csv')
df3 = pd.read_csv('C:/Users/1/Desktop/start/train/B03.csv')
df4 = pd.read_csv('C:/Users/1/Desktop/start/train/B04.csv')
df5 = pd.read_csv('C:/Users/1/Desktop/start/train/B05.csv')
df6 = pd.read_csv('C:/Users/1/Desktop/start/train/B06.csv')
df7 = pd.read_csv('C:/Users/1/Desktop/start/train/IR01.csv')
df8 = pd.read_csv('C:/Users/1/Desktop/start/train/IR02.csv')
df9 = pd.read_csv('C:/Users/1/Desktop/start/train/IR03.csv')
df10 = pd.read_csv('C:/Users/1/Desktop/start/train/IR04.csv')
df11 = pd.read_csv('C:/Users/1/Desktop/start/train/IR05.csv')
df12 = pd.read_csv('C:/Users/1/Desktop/start/train/IR06.csv')
df13 = pd.read_csv('C:/Users/1/Desktop/start/train/OR01.csv')
df14 = pd.read_csv('C:/Users/1/Desktop/start/train/OR02.csv')
df15 = pd.read_csv('C:/Users/1/Desktop/start/train/OR03.csv')
df16 = pd.read_csv('C:/Users/1/Desktop/start/train/OR04.csv')
df17 = pd.read_csv('C:/Users/1/Desktop/start/train/OR05.csv')
df18 = pd.read_csv('C:/Users/1/Desktop/start/train/OR06.csv')
df19 = pd.read_csv('C:/Users/1/Desktop/start/train/OR07.csv')
df20 = pd.read_csv('C:/Users/1/Desktop/start/train/OR08.csv')
df21 = pd.read_csv('C:/Users/1/Desktop/start/train/OR09.csv')
df22 = pd.read_csv('C:/Users/1/Desktop/start/train/OR10.csv')
df23 = pd.read_csv('C:/Users/1/Desktop/start/train/OR11.csv')
df24 = pd.read_csv('C:/Users/1/Desktop/start/train/OR12.csv')
df25 = pd.read_csv('C:/Users/1/Desktop/start/train/OR13.csv')
df26 = pd.read_csv('C:/Users/1/Desktop/start/train/OR14.csv')
df27 = pd.read_csv('C:/Users/1/Desktop/start/train/NORMAL01.csv')
df28 = pd.read_csv('C:/Users/1/Desktop/start/train/NORMAL02.csv')

#B样本整合
df_fault_B = pd.concat([df1,df2,df3,df4,df5,df6])
df_fault_B = df_fault_B.reset_index(drop=True)
df_fault_B = df_fault_B.drop(['BA_time'], axis=1)
df_fault_B = df_fault_B.drop(['RPM'], axis=1)
df_fault_B['label'] = 1
print(df_fault_B.shape)
#IR样本整合
df_fault_IR = pd.concat([df7,df8,df9,df10,df11,df12])
df_fault_IR = df_fault_IR.reset_index(drop=True)
df_fault_IR = df_fault_IR.drop(['BA_time'], axis=1)
df_fault_IR = df_fault_IR.drop(['RPM'], axis=1)
df_fault_IR['label'] = 2
print(df_fault_IR.shape)
#OR样本整合
df_fault_OR = pd.concat([df13,df14,df15,df16,df17,df18,df19,df20,df21,df22,df23,df24,df25,df26])
df_fault_OR = df_fault_OR.reset_index(drop=True)
df_fault_OR = df_fault_OR.drop(['BA_time'], axis=1)
df_fault_OR = df_fault_OR.drop(['RPM'],axis=1)
df_fault_OR['label'] = 3
print(df_fault_OR.shape)

#正常样本整合
df_normal = pd.concat([df27,df28])
df_normal = df_normal.reset_index(drop=True)
df_normal = df_normal.drop(['RPM'],axis=1)
df_normal['label'] = 0
print(df_normal.shape)

df_all = pd.concat([df_fault_B,df_fault_IR,df_fault_OR,df_normal])
df_all = df_all.reset_index(drop=True)
print(df_all.shape)
df_all.to_csv('C:/Users/1/Desktop/start/train/data_ALL.csv',index=False)






















