# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 19:58:10 2020

@author: DELL
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 23:09:38 2020

@author: DELL
"""
import pandas as pd
import numpy as np
import sys
import csv
import os
from scipy import stats,fftpack
from pywt import wavedec


params = {}

params['len_piece_train']=400                               #时间窗长度
params['len_piece']=400 
params['wave_layer']=5                                     #小波阶次
params['wave_layer1']=0 
params['wave_win']=38*pow(2,params['wave_layer']-1)-1       #pow：x的y次方，303
params['opath'] = 'D:/test/code/lightcsv/test_feature.csv'  #输出目录
argvs = sys.argv                            #可看做用于从外部获取参数的列表
#Raw_data=pd.read_csv('D:/test/try4.5/data_Train_fault_B.csv')
#(m,n)=Raw_data.shape #矩阵的行数m列数n，返回一个元组
try:
    a=0
    root = 'D:/test/code/cwru'                              #存放原始数据集，注意一定不要放入别的文件
    path = os.path.join(root)
    filenames = os.listdir(path)
    pathnames = [os.path.join(path, filename) for filename in filenames]
    def  one_row(arr_pic,arr_pic2,label):
          global a
          a=a+1
          arr_add=arr_pic.loc[::]                                  #通过行标签索引行数据
         
          arr_add2=arr_pic2.loc[::]
         
          listall=np.mat(arr_pic)
        
          listall2=np.mat(arr_pic2)
        
          result_list = []                                      #新建结果列
    
    
        
          
          for i in range(params['wave_layer1']+1):
                         
                         data_ave=np.mean(listall[:,:])
                         list_paraa=[data_ave]
                         result_list.extend(list_paraa)                            #
    
                         
                         data_std=np.std(listall[:,:]) #标准差
                         list_para2=[data_std]
                         result_list.extend(list_para2)                            #
                                                            
                         
                         
                         time_var = np.var(listall[:,:])
                         list_para6 = [time_var]
                         result_list.extend(list_para6)                            #
                         
                         time_amp = np.abs(listall[:,:]).mean()
                         list_para7 = [time_amp]
                         result_list.extend(list_para7)                            #
                         
                         time_smr = np.square(np.sqrt(np.abs(listall[:,:]).astype(np.float64)).mean())
                         list_para8 = [time_smr]
                         result_list.extend(list_para8)                            #  
                         
                         time_rms = np.sqrt(np.square(listall[:,:]).mean().astype(np.float64))
                         list_para81 = [time_rms]
                         result_list.extend(list_para81)                           #
                         
                         
                         
                         time_iqr = np.percentile(listall[:,:],75)-np.percentile(listall[:,:],25) 
                         list_para84 = [time_iqr]
                         result_list.extend(list_para84)           #
                         
                         
                         time_pr = np.percentile(listall[:,:],90)-np.percentile(listall[:,:],10)
                         list_para85 = [time_pr]
                         result_list.extend(list_para85)#最好加上                   #
                         
                         
                         
                         time_max = listall[:,:].max()
                         list_para87 = [time_max]             
                         result_list.extend(list_para87)                    
                         
                         time_min = listall[:,:].min()
                         list_para88 = [time_min]
                         result_list.extend(list_para88)                       #
                         
                         data_avep1=np.mean(listall[:,:])+1
                         list_paraap1=[data_avep1]
                         result_list.extend(list_paraap1)      #     #
                        
                         
                         if time_amp==0:
                             time_wavefactor = 0
                             time_pulse=0
                         else:
                             time_wavefactor=time_rms/time_amp
                             time_pulse = time_max/time_amp
                            
                         list_para89 = [time_wavefactor]            #擅长判3         #
                         result_list.extend(list_para89)                         #
                         
                         
                         
                         for i in arr_add.columns:
                             df_fftline = fftpack.fft(arr_add[i])
                             freq_fftline = fftpack.fftfreq(len(arr_add[i]),1/12000)
                             df_fftline = abs(df_fftline[freq_fftline>=0])
                             freq_fftline = freq_fftline[freq_fftline>=0]
                              #基本特征,依次为均值，标准差，最大值，最小值，均方根，中位数，四分位差，百分位差
                             freq_mean = df_fftline.mean()
                             freq_std = df_fftline.std()
                             freq_max = df_fftline.max()
                             freq_min = df_fftline.min()
                             freq_rms = np.sqrt(np.square(df_fftline).mean())
                             freq_median = np.median(df_fftline)
                             freq_iqr = np.percentile(df_fftline,75)-np.percentile(df_fftline,25)
                             freq_pr = np.percentile(df_fftline,90)-np.percentile(df_fftline,10)
                    #f2 f3 f4反映频谱集中程度
                             freq_f2 = np.square((df_fftline-freq_mean)).sum()/(len(df_fftline)-1)
                             freq_f3 = pow((df_fftline-freq_mean),3).sum()/(len(df_fftline)*pow(freq_f2,1.5))
                             freq_f4 = pow((df_fftline-freq_mean),4).sum()/(len(df_fftline)*pow(freq_f2,2))
                    #f5 f6 f7 f8反映主频带位置
                             freq_f5 = np.multiply(freq_fftline,df_fftline).sum()/df_fftline.sum()
                             freq_f6 = np.sqrt(np.multiply(np.square(freq_fftline),df_fftline).sum())/df_fftline.sum()
                             freq_f7 = np.sqrt(np.multiply(pow(freq_fftline,4),df_fftline).sum())/np.multiply(np.square(freq_fftline),df_fftline).sum()
                             freq_f8 = np.multiply(np.square(freq_fftline),df_fftline).sum()/np.sqrt(np.multiply(pow(freq_fftline,4),df_fftline).sum()*df_fftline.sum())
                    #----------  timefreq-domain feature,12
                    #5级小波变换，最后输出6个能量特征和其归一化能量特征
                             cA5, cD5, cD4, cD3, cD2, cD1 = wavedec(arr_add[i], 'db10', level=5)
                             ener_cA5 = np.square(cA5).sum()
                             ener_cD5 = np.square(cD5).sum()
                             ener_cD4 = np.square(cD4).sum()
                             ener_cD3 = np.square(cD3).sum()
                             ener_cD2 = np.square(cD2).sum()
                             ener_cD1 = np.square(cD1).sum()
                             ener = ener_cA5 + ener_cD1 + ener_cD2 + ener_cD3 + ener_cD4 + ener_cD5
                             
                             ratio_cA5 = ener_cA5/ener
                             ratio_cD5 = ener_cD5/ener
                             ratio_cD4 = ener_cD4/ener
                             ratio_cD3 = ener_cD3/ener
                             ratio_cD2 = ener_cD2/ener
                             ratio_cD1 = ener_cD1/ener
                             result_list.extend([freq_mean,freq_std,freq_max,freq_min,freq_rms,freq_median,freq_iqr,freq_pr,freq_f2,freq_f3,freq_f4,freq_f5,
                                                 freq_f6,freq_f7,freq_f8,ener_cA5,ener_cD5,ener_cD4,ener_cD3,ener_cD2,ener_cD1,ratio_cA5,ratio_cD5,ratio_cD4,
                                                 ratio_cD3,ratio_cD2,ratio_cD1])
                          #,,freq_median,大猛料
                         #罪魁祸首freq_meanfreq_std,ener_cD5,ener_cD4,ener_cD3,ener_cD2,ener_cD1,freq_iqrfreq_f6,freq_f5,freq_f2,freq_max,freq_min,freq_rms
                         #freq_f4,,freq_f3,ratio_cA5
                         
                         data_std2=np.std(listall2[:,:]) #标准差  无功无过
                         list_para11=[data_std2]
                         result_list.extend(list_para11)
                         
                         
                         data_energy2=np.sum(np.abs(listall2[:,:])) #能量 擅长判2
                         list_para12=[data_energy2]
                         result_list.extend(list_para12)
    
                         time_kurtosis = stats.kurtosis(listall2[:,:])
                         time_kurtosisex=np.sum(time_kurtosis)
                         list_para13 = [time_kurtosisex]
                         result_list.extend(list_para13)
                         
                         time_var = np.var(listall2[:,:])
                         list_para14 = [time_var]
                         result_list.extend(list_para14)
                         
                         time_amp = np.abs(listall2[:,:]).mean()
                         list_para15 = [time_amp]
                         result_list.extend(list_para15)
                         
                         time_smr = np.square(np.sqrt(np.abs(listall2[:,:]).astype(np.float64)).mean())
                         list_para16 = [time_smr]
                         result_list.extend(list_para16)
                         
                         time_rms = np.sqrt(np.square(listall2[:,:]).mean().astype(np.float64))
                         list_para161 = [time_rms]
                         result_list.extend(list_para161)
                         
                         time_ptp = np.asarray(listall2[:,:]).ptp()
                         list_para162 = [time_ptp]
                         result_list.extend(list_para162)
                         
                         
                         
                         time_iqr = np.percentile(listall2[:,:],75)-np.percentile(listall2[:,:],25)
                         list_para164 = [time_iqr]
                         result_list.extend(list_para164)
                         
                         
                         time_pr = np.percentile(listall2[:,:],90)-np.percentile(listall2[:,:],10)
                         list_para165 = [time_pr]
                         result_list.extend(list_para165)
                         
                         time_skew = stats.skew(listall[:,:])
                         time_skewex=np.sum(time_skew)
                         list_para166 = [time_skewex]
                         result_list.extend(list_para166)
                         
                         
                         time_min = listall2[:,:].min()
                         list_para168 = [time_min]
                         
                         result_list.extend(list_para168)
                         
                         if time_amp==0:
                             time_wavefactor = 0
                             time_pulse=0
                         else:
                             time_wavefactor=time_rms/time_amp
                             time_pulse = time_max/time_amp
                            
                         list_para169 = [time_wavefactor]
                         result_list.extend(list_para169)
                         list_para1610 = [time_pulse]
                         result_list.extend(list_para1610)
                         if time_rms==0:
                             time_peakfactor=0
                         else:
                             time_peakfactor = time_max/time_rms
                         list_para1611 = [time_peakfactor]
                         result_list.extend(list_para1611)
                         
                         if time_smr==0:
                             time_margin=0
                         else:
                             time_margin = time_max/time_smr
                         list_para1612 = [time_margin]
                         result_list.extend(list_para1612)
                         for i in arr_add2.columns:
                             df_fftline = fftpack.fft(arr_add2[i])
                             freq_fftline = fftpack.fftfreq(len(arr_add2[i]),1/12000)
                             df_fftline = abs(df_fftline[freq_fftline>=0])
                             freq_fftline = freq_fftline[freq_fftline>=0]
                              #基本特征,依次为均值，标准差，最大值，最小值，均方根，中位数，四分位差，百分位差
                             freq_mean = df_fftline.mean()
                             freq_std = df_fftline.std()
                             freq_max = df_fftline.max()
                             freq_min = df_fftline.min()
                             freq_rms = np.sqrt(np.square(df_fftline).mean())
                             freq_median = np.median(df_fftline)
                             freq_iqr = np.percentile(df_fftline,75)-np.percentile(df_fftline,25)
                             freq_pr = np.percentile(df_fftline,90)-np.percentile(df_fftline,10)
                    #f2 f3 f4反映频谱集中程度
                             freq_f2 = np.square((df_fftline-freq_mean)).sum()/(len(df_fftline)-1)
                             freq_f3 = pow((df_fftline-freq_mean),3).sum()/(len(df_fftline)*pow(freq_f2,1.5))
                             freq_f4 = pow((df_fftline-freq_mean),4).sum()/(len(df_fftline)*pow(freq_f2,2))
                    #f5 f6 f7 f8反映主频带位置
                             freq_f5 = np.multiply(freq_fftline,df_fftline).sum()/df_fftline.sum()
                             freq_f6 = np.sqrt(np.multiply(np.square(freq_fftline),df_fftline).sum())/df_fftline.sum()
                             freq_f7 = np.sqrt(np.multiply(pow(freq_fftline,4),df_fftline).sum())/np.multiply(np.square(freq_fftline),df_fftline).sum()
                             freq_f8 = np.multiply(np.square(freq_fftline),df_fftline).sum()/np.sqrt(np.multiply(pow(freq_fftline,4),df_fftline).sum()*df_fftline.sum())
                    #----------  timefreq-domain feature,12
                    #5级小波变换，最后输出6个能量特征和其归一化能量特征
                             cA5, cD5, cD4, cD3, cD2, cD1 = wavedec(arr_add2[i], 'db10', level=5)
                             ener_cA5 = np.square(cA5).sum()
                             ener_cD5 = np.square(cD5).sum()
                             ener_cD4 = np.square(cD4).sum()
                             ener_cD3 = np.square(cD3).sum()
                             ener_cD2 = np.square(cD2).sum()
                             ener_cD1 = np.square(cD1).sum()
                             ener = ener_cA5 + ener_cD1 + ener_cD2 + ener_cD3 + ener_cD4 + ener_cD5
                             ratio_cA5 = ener_cA5/ener
                             ratio_cD5 = ener_cD5/ener
                             ratio_cD4 = ener_cD4/ener
                             ratio_cD3 = ener_cD3/ener
                             ratio_cD2 = ener_cD2/ener
                             ratio_cD1 = ener_cD1/ener
                             result_list.extend([freq_mean,freq_std,freq_max,freq_min,freq_rms,freq_median,freq_iqr,freq_pr,freq_f2,freq_f3,freq_f4,freq_f5,
                                                 freq_f6,freq_f7,freq_f8,ener_cA5,ener_cD5,ener_cD4,ener_cD3,ener_cD2,ener_cD1,ratio_cA5,ratio_cD5,ratio_cD4,
                                                 ratio_cD3,ratio_cD2,ratio_cD1])
                             
                             #不能要的,freq_f3,ener_cD5,freq_mean,,freq_f6]freq_max,freq_min,freq_rms,freq_median,freq_iqr,freq_pr,freq_f2,ener_cD4,ener_cD3,ener_cD2,ener_cD1,freq_f4ratio_cA5
                             a=438
                             #无功无过
                             result_list.extend([label])
          return result_list
                             
    
    def writeit():
        
          
            for i in range(len(argvs)):   
                                             
                if i < 1:
                    continue
                    
                if argvs[i].split('=')[1] == 'None':      #以=为分隔符，分割所有，如果没有第二项
                    
                    params[argvs[i].split('=')[0]] = None  #那就把第一项也设空
                else:
                    Type = type(params[argvs[i].split('=')[0]])  #type是argvs第一项的type
                    params[argvs[i].split('=')[0]] = Type(argvs[i].split('=')[1])	
            
            data_out=[] 
            data_head=[]                               #新建data_head
            head_out=[]                                #新建head_out           	
                
            head_out=['data_ave', 'data_std', 'DE_time_var', 'DE_time_amp', 'DE_time_smr',
                          'DE_time_rms', 'DE_time_iqr', 'DE_time_pr', 'DE_max', 'DE_min',
                          'DE_avep1', 'DE_time_wavefactor', 'DE_freq_mean', 'DE_freq_std',
                          'DE_freq_max', 'DE_freq_min', 'DE_freq_rms', 'DE_freq_median',
                          'DE_freq_iqr', 'DE_freq_pr', 'DE_freq_f2', 'DE_freq_f3', 'DE_freq_f4',
                          'DE_freq_f5', 'DE_freq_f6', 'DE_freq_f7', 'DE_freq_f8', 'DE_ener_cA5',
                          'DE_ener_cD5', 'DE_ener_cD4', 'DE_ener_cD3', 'DE_ener_cD2',
                          'DE_ener_cD1', 'DE_ratio_cA5', 'DE_ratio_cD5', 'DE_ratio_cD4',
                          'DE_ratio_cD3', 'DE_ratio_cD2', 'DE_ratio_cD1', 'FE_std',
                          'time_energy2', 'time_kurtosis', 'time_var', 'time_amp', 'time_smr',
                          'time_rms', 'time_ptp', 'time_iqr', 'time_pr', 'skew', 'min',
                          'time_wavefactor', 'time_pulse', 'time_peakfactor', 'time_margin',
                          'freq_mean', 'freq_std', 'freq_max', 'freq_min', 'freq_rms',
                          'freq_median', 'freq_iqr', 'freq_pr', 'freq_f2', 'freq_f3', 'freq_f4',
                          'freq_f5', 'freq_f6', 'freq_f7', 'freq_f8', 'ener_cA5', 'ener_cD5',
                          'ener_cD4', 'ener_cD3', 'ener_cD2', 'ener_cD1', 'ratio_cA5',
                          'ratio_cD5', 'ratio_cD4', 'ratio_cD3', 'ratio_cD2', 'ratio_cD1','label']
               
            data_head.extend(head_out)
               
                
            data_out.append(data_head)                 #先导入head
            label=1
            for indexx in range(len(pathnames)):
                    list_str = str(pathnames[indexx])
                    filepath,fullflname = os.path.split(list_str)
                    fname,ext = os.path.splitext(fullflname)
                    list_str = ''.join(list_str)
                    with open(list_str,'r') as f:            #只读方式读取，f不是float
                
                        reader = csv.reader(f)                 # 使用csv的reader()方法，创建一个reader对象
                        head_row=next(reader)
                        #  head_label=head_row[-1]                #head_label=头行最后一个元素
                        head_row=head_row[:]                 #除最后一个取全部
                        # head_label2=head_row[-1]               #第二个label是倒数第二个元素
                        
                        
                        
                        
                        df = pd.read_csv(list_str)#读取csv文件
                        data=[]
                    
                        data=np.array(df)               #转化成np数组
                   
                        lenth=data[:,-1]                 #读所有行最后一个数据
                    
                        lenth=len(np.array(lenth))       #求得行数
                        i=1
                        arr_pic=[]
                        arr_pic2=[]
                        
                        while i*params['len_piece']<lenth:
                            arr_pic=df.loc[(i-1)*params['len_piece']:i*params['len_piece']-1,:'DE_time']
                
                            arr_pic2=df.loc[(i-1)*params['len_piece']:i*params['len_piece']-1,'FE_time':'FE_time']
                         
                           # label_pic=df.loc[(i-1)*params['len_piece']:i*params['len_piece']-1,'onit']       
                            i=i+1
                
                            data_out.append(one_row(arr_pic,arr_pic2,label))
                            
                        if params['len_piece']>lenth:
                            arr_pic=df.loc[:lenth,:]
                           # label_pic=df.loc[:lenth,'onit']
                        else:
                    
                            arr_pic=df.loc[lenth-params['len_piece']:lenth,:'DE_time']
                            arr_pic2=df.loc[lenth-params['len_piece']:lenth,'FE_time':'FE_time']
                           # label_pic=df.loc[lenth-params['len_piece']:lenth,'onit']
                            data_out.append(one_row(arr_pic,arr_pic2,label))
                            label=label+1
           
            return data_out
     
    h=1
    #测试集特征提取
    predata=[]
    
    outstrings=params['opath']    
    predata=writeit()
    wrtocsv = pd.DataFrame(predata)
    wrtocsv.to_csv(outstrings,index=False,header=False)
        #训练集特征提取

except Exception as e:
    print(e)