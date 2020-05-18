# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 16:54:54 2020

@author: DELL
"""
from sklearn.neighbors import KNeighborsClassifier
import joblib
import numpy as np
import pandas as pd

path1 = 'D:/test/try4.5/datacsv_test/data_valid_normal_feature.csv'  #特征提取后的csv文件路径
df = pd.DataFrame(pd.read_csv(path1))
delete_features = ['ratio_cA5','ratio_cD5','ratio_cD4','ratio_cD3','ratio_cD2','ratio_cD1','time_wavefactor','time_pulse','time_peakfactor','freq_f5','freq_f8','DE_ratio_cA5','DE_ratio_cD5','DE_ratio_cD4','DE_ratio_cD3','DE_ratio_cD2','DE_ratio_cD1','DE_freq_f8'] #需要删除的列名自行加到数组里
df = df.drop(delete_features, axis=1) #特征选择之后的数据
df.to_csv(path1,index=False,header=True)
path2 = 'D:/test/try4.5/datacsv_test/data_valid_fault_B_feature.csv' #特征提取后的csv文件路径
df = pd.DataFrame(pd.read_csv(path2))
delete_features = ['ratio_cA5','ratio_cD5','ratio_cD4','ratio_cD3','ratio_cD2','ratio_cD1','time_wavefactor','time_pulse','time_peakfactor','freq_f5','freq_f8','DE_ratio_cA5','DE_ratio_cD5','DE_ratio_cD4','DE_ratio_cD3','DE_ratio_cD2','DE_ratio_cD1','DE_freq_f8'] #需要删除的列名自行加到数组里
df = df.drop(delete_features, axis=1) #特征选择之后的数据
df.to_csv(path2,index=False,header=True)
path3 = 'D:/test/try4.5/datacsv_test/data_valid_fault_OR_feature.csv' #特征提取后的csv文件路径
df = pd.DataFrame(pd.read_csv(path3))
delete_features = ['ratio_cA5','ratio_cD5','ratio_cD4','ratio_cD3','ratio_cD2','ratio_cD1','time_wavefactor','time_pulse','time_peakfactor','freq_f5','freq_f8','DE_ratio_cA5','DE_ratio_cD5','DE_ratio_cD4','DE_ratio_cD3','DE_ratio_cD2','DE_ratio_cD1','DE_freq_f8'] #需要删除的列名自行加到数组里
df = df.drop(delete_features, axis=1) #特征选择之后的数据
df.to_csv(path3,index=False,header=True)
path4 ='D:/test/try4.5/datacsv_test/data_valid_fault_IR_feature.csv' #特征提取后的csv文件路径
df = pd.DataFrame(pd.read_csv(path4))
delete_features = ['ratio_cA5','ratio_cD5','ratio_cD4','ratio_cD3','ratio_cD2','ratio_cD1','time_wavefactor','time_pulse','time_peakfactor','freq_f5','freq_f8','DE_ratio_cA5','DE_ratio_cD5','DE_ratio_cD4','DE_ratio_cD3','DE_ratio_cD2','DE_ratio_cD1','DE_freq_f8'] #需要删除的列名自行加到数组里
df = df.drop(delete_features, axis=1) #特征选择之后的数据
df.to_csv(path4,index=False,header=True)
path5 = 'D:/test/try4.5/datacsv_test/data_Train_normal_feature.csv' #特征提取后的csv文件路径
df = pd.DataFrame(pd.read_csv(path5))
delete_features = ['ratio_cA5','ratio_cD5','ratio_cD4','ratio_cD3','ratio_cD2','ratio_cD1','time_wavefactor','time_pulse','time_peakfactor','freq_f5','freq_f8','DE_ratio_cA5','DE_ratio_cD5','DE_ratio_cD4','DE_ratio_cD3','DE_ratio_cD2','DE_ratio_cD1','DE_freq_f8'] #需要删除的列名自行加到数组里
df = df.drop(delete_features, axis=1) #特征选择之后的数据
df.to_csv(path5,index=False,header=True)
path6 = 'D:/test/try4.5/datacsv_test/data_Train_fault_B_feature.csv' #特征提取后的csv文件路径
df = pd.DataFrame(pd.read_csv(path6))
delete_features = ['ratio_cA5','ratio_cD5','ratio_cD4','ratio_cD3','ratio_cD2','ratio_cD1','time_wavefactor','time_pulse','time_peakfactor','freq_f5','freq_f8','DE_ratio_cA5','DE_ratio_cD5','DE_ratio_cD4','DE_ratio_cD3','DE_ratio_cD2','DE_ratio_cD1','DE_freq_f8'] #需要删除的列名自行加到数组里
df = df.drop(delete_features, axis=1) #特征选择之后的数据
df.to_csv(path6,index=False,header=True)
path7 = 'D:/test/try4.5/datacsv_test/data_Train_fault_IR_feature.csv' #特征提取后的csv文件路径
df = pd.DataFrame(pd.read_csv(path7))
delete_features = ['ratio_cA5','ratio_cD5','ratio_cD4','ratio_cD3','ratio_cD2','ratio_cD1','time_wavefactor','time_pulse','time_peakfactor','freq_f5','freq_f8','DE_ratio_cA5','DE_ratio_cD5','DE_ratio_cD4','DE_ratio_cD3','DE_ratio_cD2','DE_ratio_cD1','DE_freq_f8'] #需要删除的列名自行加到数组里
df = df.drop(delete_features, axis=1) #特征选择之后的数据
df.to_csv(path7,index=False,header=True)
path8 = 'D:/test/try4.5/datacsv_test/data_Train_fault_OR_feature.csv'  #特征提取后的csv文b=13件路径
df = pd.DataFrame(pd.read_csv(path8))
delete_features = ['ratio_cA5','ratio_cD5','ratio_cD4','ratio_cD3','ratio_cD2','ratio_cD1','time_wavefactor','time_pulse','time_peakfactor','freq_f5','freq_f8','DE_ratio_cA5','DE_ratio_cD5','DE_ratio_cD4','DE_ratio_cD3','DE_ratio_cD2','DE_ratio_cD1','DE_freq_f8'] #需要删除的列名自行加到数组里
df = df.drop(delete_features, axis=1) #特征选择之后的数据
df.to_csv(path8,index=False,header=True)




test_m1 = pd.DataFrame(pd.read_csv('D:/test/try4.5/datacsv_test/data_test1_feature.csv'))
delete_features = ['ratio_cA5','ratio_cD5','ratio_cD4','ratio_cD3','ratio_cD2','ratio_cD1','time_wavefactor','time_pulse','time_peakfactor','freq_f5','freq_f8','DE_ratio_cA5','DE_ratio_cD5','DE_ratio_cD4','DE_ratio_cD3','DE_ratio_cD2','DE_ratio_cD1','DE_freq_f8'] #需要删除的列名自行加到数组里
test_m1 = test_m1.drop(delete_features, axis=1) #特征选择之后的数据
test_m1.to_csv('D:/test/try4.5/datacsv_test/data_test1_feature.csv',index=False,header=True)
test_m2 = pd.DataFrame(pd.read_csv('D:/test/try4.5/datacsv_test/data_test2_feature.csv'))
delete_features = ['ratio_cA5','ratio_cD5','ratio_cD4','ratio_cD3','ratio_cD2','ratio_cD1','time_wavefactor','time_pulse','time_peakfactor','freq_f5','freq_f8','DE_ratio_cA5','DE_ratio_cD5','DE_ratio_cD4','DE_ratio_cD3','DE_ratio_cD2','DE_ratio_cD1','DE_freq_f8'] #需要删除的列名自行加到数组里
test_m2 = test_m2.drop(delete_features, axis=1) #特征选择之后的数据
test_m2.to_csv('D:/test/try4.5/datacsv_test/data_test2_feature.csv',index=False,header=True)
test_m3 = pd.DataFrame(pd.read_csv('D:/test/try4.5/datacsv_test/data_test3_feature.csv'))
delete_features = ['ratio_cA5','ratio_cD5','ratio_cD4','ratio_cD3','ratio_cD2','ratio_cD1','time_wavefactor','time_pulse','time_peakfactor','freq_f5','freq_f8','DE_ratio_cA5','DE_ratio_cD5','DE_ratio_cD4','DE_ratio_cD3','DE_ratio_cD2','DE_ratio_cD1','DE_freq_f8'] #需要删除的列名自行加到数组里
test_m3 = test_m3.drop(delete_features, axis=1) #特征选择之后的数据
test_m3.to_csv('D:/test/try4.5/datacsv_test/data_test3_feature.csv',index=False,header=True)
test_m4 = pd.DataFrame(pd.read_csv('D:/test/try4.5/datacsv_test/data_test4_feature.csv'))
delete_features = ['ratio_cA5','ratio_cD5','ratio_cD4','ratio_cD3','ratio_cD2','ratio_cD1','time_wavefactor','time_pulse','time_peakfactor','freq_f5','freq_f8','DE_ratio_cA5','DE_ratio_cD5','DE_ratio_cD4','DE_ratio_cD3','DE_ratio_cD2','DE_ratio_cD1','DE_freq_f8'] #需要删除的列名自行加到数组里
test_m4 = test_m4.drop(delete_features, axis=1) #特征选择之后的数据
test_m4.to_csv('D:/test/try4.5/datacsv_test/data_test4_feature.csv',index=False,header=True)
test_m5 = pd.DataFrame(pd.read_csv('D:/test/try4.5/datacsv_test/data_test5_feature.csv'))
delete_features = ['ratio_cA5','ratio_cD5','ratio_cD4','ratio_cD3','ratio_cD2','ratio_cD1','time_wavefactor','time_pulse','time_peakfactor','freq_f5','freq_f8','DE_ratio_cA5','DE_ratio_cD5','DE_ratio_cD4','DE_ratio_cD3','DE_ratio_cD2','DE_ratio_cD1','DE_freq_f8'] #需要删除的列名自行加到数组里
test_m5 = test_m5.drop(delete_features, axis=1) #特征选择之后的数据
test_m5.to_csv('D:/test/try4.5/datacsv_test/data_test5_feature.csv',index=False,header=True)
test_m6 = pd.DataFrame(pd.read_csv('D:/test/try4.5/datacsv_test/data_test6_feature.csv'))
delete_features = ['ratio_cA5','ratio_cD5','ratio_cD4','ratio_cD3','ratio_cD2','ratio_cD1','time_wavefactor','time_pulse','time_peakfactor','freq_f5','freq_f8','DE_ratio_cA5','DE_ratio_cD5','DE_ratio_cD4','DE_ratio_cD3','DE_ratio_cD2','DE_ratio_cD1','DE_freq_f8'] #需要删除的列名自行加到数组里
test_m6 = test_m6.drop(delete_features, axis=1) #特征选择之后的数据
test_m6.to_csv('D:/test/try4.5/datacsv_test/data_test6_feature.csv',index=False,header=True)
test_m7 = pd.DataFrame(pd.read_csv('D:/test/try4.5/datacsv_test/data_test7_feature.csv'))
delete_features = ['ratio_cA5','ratio_cD5','ratio_cD4','ratio_cD3','ratio_cD2','ratio_cD1','time_wavefactor','time_pulse','time_peakfactor','freq_f5','freq_f8','DE_ratio_cA5','DE_ratio_cD5','DE_ratio_cD4','DE_ratio_cD3','DE_ratio_cD2','DE_ratio_cD1','DE_freq_f8'] #需要删除的列名自行加到数组里
test_m7 = test_m7.drop(delete_features, axis=1) #特征选择之后的数据
test_m7.to_csv('D:/test/try4.5/datacsv_test/data_test7_feature.csv',index=False,header=True)
test_m8 = pd.DataFrame(pd.read_csv('D:/test/try4.5/datacsv_test/data_test8_feature.csv'))
delete_features = ['ratio_cA5','ratio_cD5','ratio_cD4','ratio_cD3','ratio_cD2','ratio_cD1','time_wavefactor','time_pulse','time_peakfactor','freq_f5','freq_f8','DE_ratio_cA5','DE_ratio_cD5','DE_ratio_cD4','DE_ratio_cD3','DE_ratio_cD2','DE_ratio_cD1','DE_freq_f8'] #需要删除的列名自行加到数组里
test_m8 = test_m8.drop(delete_features, axis=1) #特征选择之后的数据
test_m8.to_csv('D:/test/try4.5/datacsv_test/data_test8_feature.csv',index=False,header=True)
test_m9 = pd.DataFrame(pd.read_csv('D:/test/try4.5/datacsv_test/data_test9_feature.csv'))
delete_features = ['ratio_cA5','ratio_cD5','ratio_cD4','ratio_cD3','ratio_cD2','ratio_cD1','time_wavefactor','time_pulse','time_peakfactor','freq_f5','freq_f8','DE_ratio_cA5','DE_ratio_cD5','DE_ratio_cD4','DE_ratio_cD3','DE_ratio_cD2','DE_ratio_cD1','DE_freq_f8'] #需要删除的列名自行加到数组里
test_m9 = test_m9.drop(delete_features, axis=1) #特征选择之后的数据
test_m9.to_csv('D:/test/try4.5/datacsv_test/data_test9_feature.csv',index=False,header=True)
test_m10 = pd.DataFrame(pd.read_csv('D:/test/try4.5/datacsv_test/data_test10_feature.csv'))
delete_features = ['ratio_cA5','ratio_cD5','ratio_cD4','ratio_cD3','ratio_cD2','ratio_cD1','time_wavefactor','time_pulse','time_peakfactor','freq_f5','freq_f8','DE_ratio_cA5','DE_ratio_cD5','DE_ratio_cD4','DE_ratio_cD3','DE_ratio_cD2','DE_ratio_cD1','DE_freq_f8'] #需要删除的列名自行加到数组里
test_m10= test_m10.drop(delete_features, axis=1) #特征选择之后的数据
test_m10.to_csv('D:/test/try4.5/datacsv_test/data_test10_feature.csv',index=False,header=True)
test_m11 = pd.DataFrame(pd.read_csv('D:/test/try4.5/datacsv_test/data_test11_feature.csv'))
delete_features = ['ratio_cA5','ratio_cD5','ratio_cD4','ratio_cD3','ratio_cD2','ratio_cD1','time_wavefactor','time_pulse','time_peakfactor','freq_f5','freq_f8','DE_ratio_cA5','DE_ratio_cD5','DE_ratio_cD4','DE_ratio_cD3','DE_ratio_cD2','DE_ratio_cD1','DE_freq_f8'] #需要删除的列名自行加到数组里
test_m11 = test_m11.drop(delete_features, axis=1) #特征选择之后的数据
test_m11.to_csv('D:/test/try4.5/datacsv_test/data_test11_feature.csv',index=False,header=True)
test_m12 = pd.DataFrame(pd.read_csv('D:/test/try4.5/datacsv_test/data_test12_feature.csv'))
delete_features = ['ratio_cA5','ratio_cD5','ratio_cD4','ratio_cD3','ratio_cD2','ratio_cD1','time_wavefactor','time_pulse','time_peakfactor','freq_f5','freq_f8','DE_ratio_cA5','DE_ratio_cD5','DE_ratio_cD4','DE_ratio_cD3','DE_ratio_cD2','DE_ratio_cD1','DE_freq_f8'] #需要删除的列名自行加到数组里
test_m12 = test_m12.drop(delete_features, axis=1) #特征选择之后的数据
test_m12.to_csv('D:/test/try4.5/datacsv_test/data_test12_feature.csv',index=False,header=True)
test_m13 = pd.DataFrame(pd.read_csv('D:/test/try4.5/datacsv_test/data_test13_feature.csv'))
delete_features = ['ratio_cA5','ratio_cD5','ratio_cD4','ratio_cD3','ratio_cD2','ratio_cD1','time_wavefactor','time_pulse','time_peakfactor','freq_f5','freq_f8','DE_ratio_cA5','DE_ratio_cD5','DE_ratio_cD4','DE_ratio_cD3','DE_ratio_cD2','DE_ratio_cD1','DE_freq_f8'] #需要删除的列名自行加到数组里
test_m13 = test_m13.drop(delete_features, axis=1) #特征选择之后的数据
test_m13.to_csv('D:/test/try4.5/datacsv_test/data_test13_feature.csv',index=False,header=True)
test_m14 = pd.DataFrame(pd.read_csv('D:/test/try4.5/datacsv_test/data_test14_feature.csv'))
delete_features = ['ratio_cA5','ratio_cD5','ratio_cD4','ratio_cD3','ratio_cD2','ratio_cD1','time_wavefactor','time_pulse','time_peakfactor','freq_f5','freq_f8','DE_ratio_cA5','DE_ratio_cD5','DE_ratio_cD4','DE_ratio_cD3','DE_ratio_cD2','DE_ratio_cD1','DE_freq_f8'] #需要删除的列名自行加到数组里
test_m14 = test_m14.drop(delete_features, axis=1) #特征选择之后的数据
test_m14.to_csv('D:/test/try4.5/datacsv_test/data_test14_feature.csv',index=False,header=True)
#'ratio_cA5','ratio_cD5','ratio_cD4','ratio_cD3','ratio_cD2','ratio_cD1'
#'time_wavefactor','time_pulse','time_peakfactor','freq_f5','freq_f8','DE_ratio_cA5','DE_ratio_cD5','DE_ratio_cD4','DE_ratio_cD3','DE_ratio_cD2','DE_ratio_cD1','DE_freq_f8'



