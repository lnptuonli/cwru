import pandas
 
data = pandas.read_csv('D:/test/try4.5/data_Train_fault_B_featureall.csv')
 
 
# 导入线性回归方程和模型选择方法
 
 
from sklearn.linear_model import LinearRegression
 
from sklearn.feature_selection import SelectFromModel
 
 
# 自变量特征
 
feature=data[['data_ave','data_std','DE_time_var','DE_time_amp','DE_time_smr','DE_time_rms','DE_time_iqr','DE_time_pr','DE_max','DE_min','DE_avep1','DE_time_wavefactor',
                      'DE_freq_mean','DE_freq_std','DE_freq_max','DE_freq_min','DE_freq_rms','DE_freq_median','DE_freq_iqr','DE_freq_pr','DE_freq_f2',
                      'DE_freq_f3','DE_freq_f4','DE_freq_f5','DE_freq_f6','DE_freq_f7','DE_freq_f8',
                      'DE_ener_cA5','DE_ener_cD5','DE_ener_cD4','DE_ener_cD3','DE_ener_cD2','DE_ener_cD1','DE_ratio_cA5','DE_ratio_cD5','DE_ratio_cD4',
                      'DE_ratio_cD3','DE_ratio_cD2','DE_ratio_cD1',
                     'FE_std','time_energy2','time_kurtosis','time_var','time_amp','time_smr','time_rms','time_ptp','time_iqr','time_pr','skew',
                     'min','time_wavefactor','time_pulse','time_peakfactor','time_margin','freq_mean','freq_std','freq_max','freq_min','freq_rms','freq_median',
                     'freq_iqr','freq_pr','freq_f2','freq_f3','freq_f4','freq_f5','freq_f6','freq_f7','freq_f8','ener_cA5','ener_cD5','ener_cD4','ener_cD3','ener_cD2',
                     'ener_cD1','ratio_cA5','ratio_cD5','ratio_cD4','ratio_cD3','ratio_cD2','ratio_cD1']]
 
# 建立线性回归模型
 
LrModel= LinearRegression()
 
# 建立选择回归模型
 
selectFromModel= SelectFromModel(LrModel)
 
# fit方法训练选择，自动选择最优的特征数
 
selectFromModel.fit_transform(
        feature,
        data['label']
        )
bce=feature.columns[selectFromModel.get_support()] 
print(bce)
