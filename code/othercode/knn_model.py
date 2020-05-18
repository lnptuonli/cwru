from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import pandas as pd
import os
import joblib
import operator

#要修改训练文件地址
def train_model_knn():
    train_data_B = pd.read_csv('C:/Users/1/Desktop/start/featureget/data_Train_fault_B_feature.csv')
    train_data_B['label'] = 1
    train_data_IR = pd.read_csv('C:/Users/1/Desktop/start/featureget/data_Train_fault_IR_feature.csv')
    train_data_IR['label'] = 3
    train_data_OR = pd.read_csv('C:/Users/1/Desktop/start/featureget/data_Train_fault_OR_feature.csv')
    train_data_OR['label'] = 2
    train_data_normal = pd.read_csv('C:/Users/1/Desktop/start/featureget/data_Train_normal_feature.csv')
    train_data_normal['label'] = 0
    
    
    train_data = pd.concat([train_data_B,train_data_IR,train_data_OR,train_data_normal])
    train_data = train_data.reset_index(drop=True)
    train_data_y = train_data['label']
    train_data_x = train_data.drop(['label'], axis=1)

    
    model_neigh_default = KNeighborsClassifier(n_neighbors=11)
    model_neigh_default.fit(train_data_x,train_data_y)
    joblib.dump(model_neigh_default, 'C:/Users/1/Desktop/start/modelKnn/KNN_model_all.model')
    #模型输出地址




train_model_knn()




