# CWRU 数据比赛 

## 项目概述
本实验针对CWRU数据集进行轴承故障分类，所实现的目标是对测试文件实现4分类——B代表故障发生在Ball位置，同理IR代表故障发生在inner race位置，OR代表故障发生在outer race位置，NORMAL代表数据文件是正常数据文件。 在PHM通用处理流程的基础上， 考虑了轴承数据的特征与分类，从特征分析与模型优化两个角度进行故障分类。

## 目录结构
```
code
├── Readme.md                   // help
├── knnf                        // 存放模型文件的文件夹
│   └── cwru.model              // 模型文件(sklearn version 0.19.2)
├── lightcsv
│   ├── test_feature.csv        // 特征提取后的文件，合成了一个文件
│   └── result.csv              // 最终的结果文件
├── cwru
│   |── TEST001.csv				// 142个原测试文件（务必是重命名过的）
│   ├── TEST002.csv             
│   ├── TEST003.csv        
│   ├── TEST004.csv                
│   ├── TEST005.csv             
│   ├── TEST006.csv       
│   └── ......              
├── othercodes                  // 开发时用到的工具
│   |── datasee.py				// 数据画图观察工具，用于初筛特征
│   ├── feature_select.py       // 特征文件列删除工具，用于观察不同文件对不同特征的敏感程度      
│   ├── featureSelection.py     // 特征文件回归模型，用于在训练集中选择与相应故障位置关系较大的特征 
│   ├── knn_model.py            // 模型训练  
│   ├── SMOTE.py                // 训练集数据预处理   
│   └── trainset.py             // 训练集数据整合

├── knn_upload(1).py            // 判断程序，用于特征提取后调用模型生成result.csv
├── featureStractV1.py			// 预处理/特征提取程序
├── result.csv					// 答案文件，应与lightcsv中的结果文件一致
└── cwru.zip					// 已经手动重命名过的测试文件
```



## 版本管理（可选，便于之后的维护）
 v1.0.0 
## 依赖配置
Python 3.7.0 [default, MSC v.1912 64 bit (AMD64)]

用到的库：

sklearn

pandas

numpy

scipy

## 部署说明
预处理与特征提取部分：

```
params['opath'] = 'D:/test/code/lightcsv/test_feature.csv'  #特征文件输出目录
root = 'D:/test/code/cwru'                              #存放原始数据集，请注意文件名要求
```

模型调用部分：

```
params['model'] = 'D:/test/code/knnf/cwru.model'           #模型文件位置
params['test']= 'D:/test/code/lightcsv/test_feature.csv'  #特征文件存放目录
params['opath']='D:/test/code/lightcsv/resultcsv'         #答案输出目录
```

## 运行说明
```
请按顺序分别执行featureStractV1.pyknn_upload(1).py文件，在lightcsv中找到result.csv即为答案
```



## 注意事项
1.本实验对测试集文件的文件名有所要求，请将测试集文件手动命名为以下格式，以免出现乱序问题

	001.csv
	002.csv
	003.csv
	004.csv
	.
	.
	.
	142.csv  #已经由我们重命名好的文件已经放在名为cwru.zip的压缩包中

2.运行时，为了简化操作步骤，我们直接用本地训练好的模型去进行预测分类。