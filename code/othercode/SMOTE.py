#训练集采用SMOTE预处理，并划分出验证集

import pandas as pd
import os
from imblearn.over_sampling import SMOTE # 过抽样处理库SMOTE
#from imblearn.under_sampling import RandomUnderSampler # 欠抽样处理库RandomUnderSampler
#from sklearn.svm import SVC #SVM中的分类算法SVC
import numpy as np
from sklearn.model_selection import train_test_split


df = pd.read_csv('C:/Users/1/Desktop/start/train/data_ALL.csv') # 读取数据文件
x = df.iloc[:, :-1] # 切片，得到输入x
y = df.iloc[:, -1] # 切片，得到标签y
groupby_data_orgianl = df.groupby('label').count() # 对label做分类汇总
print (groupby_data_orgianl) # 打印输出原始数据集样本分类分布

# 使用SMOTE方法进行过抽样处理
model_smote = SMOTE() # 建立SMOTE模型对象
x_smote_resampled, y_smote_resampled = model_smote.fit_sample(x,y) # 输入数据并作过抽样处理
x_smote_resampled = pd.DataFrame(x_smote_resampled, columns=['DE_time','FE_time', 'RPM']) # 将数据转换为数据框并命名列名
y_smote_resampled = pd.DataFrame(y_smote_resampled,columns=['label']) # 将数据转换为数据框并命名列名
smote_resampled = pd.concat([x_smote_resampled, y_smote_resampled],axis=1) # 按列合并数据框
smote_resampled = smote_resampled.drop(['RPM'], axis=1)
groupby_data_smote = smote_resampled.groupby('label').count() # 对label做分类汇总
print (groupby_data_smote) # 打印输出经过SMOTE处理后的数据集样本分类分布

fault_B = []
fault_IR = []
fault_OR = []
normal = []
h = 0
for i in smote_resampled.iloc[:,2]:
    if(i == 1):
        fault_B.append(smote_resampled.iloc[h,0])
    if(i == 2):
        fault_IR.append(smote_resampled.iloc[h,0])
    if(i == 3):
        fault_OR.append(smote_resampled.iloc[h,0])
    if(i == 0):
        normal.append(smote_resampled.iloc[h,0])
    h += 1


fault_B1 = []
fault_IR1 = []
fault_OR1 = []
normal1 = []
h = 0
for i in smote_resampled.iloc[:,2]:
    if(i == 1):
        fault_B1.append(smote_resampled.iloc[h,1])
    if(i == 2):
        fault_IR1.append(smote_resampled.iloc[h,1])
    if(i == 3):
        fault_OR1.append(smote_resampled.iloc[h,1])
    if(i == 0):
        normal1.append(smote_resampled.iloc[h,1])
    h += 1


data = np.asarray(fault_B)
data = pd.DataFrame(data,columns=["DEtime"])
####
data1 = np.asarray(fault_B1)
data1 = pd.DataFrame(data1,columns=["FEtime"])
data = data.join(data1)
####
data['label'] = 1
data = np.array(data)
data = pd.DataFrame(data,columns=[0,1,2])
#看几列删除
data.to_csv('C:/Users/1/Desktop/start/dataset/data_fault_B.csv',index=False)

data = np.asarray(fault_IR)
data = pd.DataFrame(data,columns=["DEtime"])
####
data1 = np.asarray(fault_IR1)
data1 = pd.DataFrame(data1,columns=["FEtime"])
data = data.join(data1)
####
data['label'] = 2
data = np.array(data)
data = pd.DataFrame(data,columns=[0,1,2])
#看几列删除
data.to_csv('C:/Users/1/Desktop/start/dataset/data_fault_IR.csv',index=False)

data = np.asarray(fault_OR)
data = pd.DataFrame(data,columns=["DEtime"])
####
data1 = np.asarray(fault_OR1)
data1 = pd.DataFrame(data1,columns=["FEtime"])
data = data.join(data1)
####
data['label'] = 3
data = np.array(data)
data = pd.DataFrame(data,columns=[0,1,2])
#看几列删除
data.to_csv('C:/Users/1/Desktop/start/dataset/data_fault_OR.csv',index=False)

data = np.asarray(normal)
data = pd.DataFrame(data,columns=["DEtime"])
####
data1 = np.asarray(normal1)
data1 = pd.DataFrame(data1,columns=["FEtime"])
data = data.join(data1)
####
data['label'] = 0
data = np.array(data)
data = pd.DataFrame(data,columns=[0,1,2])
data.to_csv('C:/Users/1/Desktop/start/dataset/data_normal.csv',index=False)


#划分验证集与训练集，用于测试模型
data = np.loadtxt(open('C:/Users/1/Desktop/start/dataset/data_fault_B.csv'),delimiter=",",skiprows=0)
X, y = data[:,:-1],data[:,-1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train=pd.DataFrame(X_train,columns=["DEtime","FEtime"])
X_train.to_csv('C:/Users/1/Desktop/start/datacsv/data_Train_fault_B.csv',index=False)
X_test=pd.DataFrame(X_test,columns=["DEtime","FEtime"])
X_test.to_csv('C:/Users/1/Desktop/start/datacsv/data_valid_fault_B.csv',index=False)

data = np.loadtxt(open('C:/Users/1/Desktop/start/dataset/data_fault_IR.csv'),delimiter=",",skiprows=0)
X, y = data[:,:-1],data[:,-1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train=pd.DataFrame(X_train,columns=["DEtime","FEtime"])
X_train.to_csv('C:/Users/1/Desktop/start/datacsv/data_Train_fault_IR.csv',index=False)
X_test=pd.DataFrame(X_test,columns=["DEtime","FEtime"])
X_test.to_csv('C:/Users/1/Desktop/start/datacsv/data_valid_fault_IR.csv',index=False)

data = np.loadtxt(open('C:/Users/1/Desktop/start/dataset/data_fault_OR.csv'),delimiter=",",skiprows=0)
X, y = data[:,:-1],data[:,-1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train=pd.DataFrame(X_train,columns=["DEtime","FEtime"])
X_train.to_csv('C:/Users/1/Desktop/start/datacsv/data_Train_fault_OR.csv',index=False)
X_test=pd.DataFrame(X_test,columns=["DEtime","FEtime"])
X_test.to_csv('C:/Users/1/Desktop/start/datacsv/data_valid_fault_OR.csv',index=False)

data = np.loadtxt(open('C:/Users/1/Desktop/start/dataset/data_normal.csv'),delimiter=",",skiprows=0)
X, y = data[:,:-1],data[:,-1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train=pd.DataFrame(X_train,columns=["DEtime","FEtime"])
X_train.to_csv('C:/Users/1/Desktop/start/datacsv/data_Train_normal.csv',index=False)
X_test=pd.DataFrame(X_test,columns=["DEtime","FEtime"])
X_test.to_csv('C:/Users/1/Desktop/start/datacsv/data_valid_normal.csv',index=False)































































"""
# 使用RandomUnderSampler方法进行欠抽样处理
model_RandomUnderSampler = RandomUnderSampler() # 建立RandomUnderSampler模型对象
x_RandomUnderSampler_resampled, y_RandomUnderSampler_resampled =model_RandomUnderSampler.fit_sample(x,y) # 输入数据并作欠抽样处理
x_RandomUnderSampler_resampled =pd.DataFrame(x_RandomUnderSampler_resampled,columns=['col1','col2','col3','col4','col5'])
# 将数据转换为数据框并命名列名
y_RandomUnderSampler_resampled =pd.DataFrame(y_RandomUnderSampler_resampled,columns=['label']) # 将数据转换为数据框并命名列名
RandomUnderSampler_resampled =pd.concat([x_RandomUnderSampler_resampled, y_RandomUnderSampler_resampled], axis= 1) # 按列合并数据框
groupby_data_RandomUnderSampler =RandomUnderSampler_resampled.groupby('label').count() # 对label做分类汇总
print (groupby_data_RandomUnderSampler) # 打印输出经过RandomUnderSampler处理后的数据集样本分类分布

# 使用SVM的权重调节处理不均衡样本
model_svm = SVC(class_weight='balanced') # 创建SVC模型对象并指定类别权重
model_svm.fit(x, y) # 输入x和y并训练模型

# 使用集成方法EasyEnsemble处理不均衡样本
model_EasyEnsemble = EasyEnsemble() # 建立EasyEnsemble模型对象
x_EasyEnsemble_resampled, y_EasyEnsemble_resampled = model_EasyEnsemble.fit_sample(x, y) # 输入数据并应用集成方法处理
print (x_EasyEnsemble_resampled.shape) # 打印输出集成方法处理后的x样本集概况
print (y_EasyEnsemble_resampled.shape) # 打印输出集成方法处理后的y标签集概况

# 抽取其中一份数据做审查
index_num = 1 # 设置抽样样本集索引
x_EasyEnsemble_resampled_t =pd.DataFrame(x_EasyEnsemble_resampled[index_num],columns=['col1','col2','col3','col4','col5'])
# 将数据转换为数据框并命名列名
y_EasyEnsemble_resampled_t =pd.DataFrame(y_EasyEnsemble_resampled[index_num],columns=['label']) # 将数据转换为数据框并命名列名
EasyEnsemble_resampled = pd.concat([x_EasyEnsemble_resampled_t,
y_EasyEnsemble_resampled_t], axis = 1) # 按列合并数据框
groupby_data_EasyEnsemble =EasyEnsemble_resampled.groupby('label').count() # 对label做分类汇总
print (groupby_data_EasyEnsemble) # 打印输出经过EasyEnsemble处理后的数据集样本分类分布"""
