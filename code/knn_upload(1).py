import pandas as pd
import joblib
import operator
import sys



class Result:
    explained_variance_score = 0
    mean_absolute_error = 0
    mean_squared_error = 0
    median_absolute_error =0
    r2_score=0

params = {}
"""
params['model'] = '/usr/local/data/upload/model/Model_all.model'
params['test'] = '/usr/local/data/lab_shouce/test11_selected.csv'
params['opath']='/usr/local/data/out.csv'
"""
params['model'] = 'D:/test/code/knnf/cwru.model'
params['test'] = 'D:/test/code/lightcsv/test_feature.csv'
params['opath']='D:/test/code/lightcsv/result.csv'


argvs = sys.argv
try:
    for i in range(len(argvs)):
        if i < 1:
            continue
        if argvs[i].split('=')[1] == 'None':
            params[argvs[i].split('=')[0]] = None
        else:
            Type = type(params[argvs[i].split('=')[0]])
            params[argvs[i].split('=')[0]] = Type(argvs[i].split('=')[1])
    model = joblib.load(params['model'])
    test_csv = pd.read_csv(params['test'])

    y_label = test_csv['label']
    test_csv = test_csv.drop(['label'], axis=1)
    y_pred = model.predict(test_csv)
    y_pred = pd.DataFrame(y_pred,columns=["result"])
    df = y_pred.join(y_label)

    result_file = {}
    for i in range(1,df.iloc[-1,-1]+1):
        result_file[i] = []
    h = 0
    for i in df.iloc[:,-1]:
        for j in range(1,df.iloc[-1,-1] + 1):
            if(i == j):
                result_file[j].append(df.iloc[h,0])
        h += 1



    numB = []
    numIR = []
    numOR = []
    numNormal = []

    for i in range(0,df.iloc[-1,-1]):
        numB.append(0)
        numIR.append(0)
        numOR.append(0)
        numNormal.append(0)
    j = 0
    for h in result_file:
        for i in result_file[h]:
            if(i == "1"):
                numB[j] = numB[j] + 1
            if(i == "3"):
                numIR[j] = numIR[j] + 1
            if(i == '2'):
                numOR[j] = numOR[j] + 1
            if(i == '0'):
                numNormal[j] = numNormal[j] + 1
        j = j + 1


    data = {}

    for i in range(0,df.iloc[-1,-1]):
        data['TEST'+str(i+1)] = [numNormal[i],numB[i],numOR[i],numIR[i]]
    result_index = []
    result_precison = []
    for i in data:
        data_All = [data[i][0],data[i][1],data[i][2],data[i][3]]
        max_index,max_num = max(enumerate(data_All), key = operator.itemgetter(1))
        data_sum = sum(data_All)
        result_index.append(max_index)    
        result_precison.append(max_num/data_sum)
    result_index = pd.DataFrame(result_index,columns=["label"])
    result_precison = pd.DataFrame(result_precison,columns=["precison"])

    name = []
    for h in range(0,df.iloc[-1,-1]):
        if(h+1<10):
            name.append("TEST"+str(h+1))
        elif(h+1<100):
            name.append("TEST"+str(h+1))
        else:
            name.append("TEST"+str(h+1))
    
    name = pd.DataFrame(name,columns=["filename"])

    result_index = result_index.join(name)
    result = result_index
#    result = result_index.join(result_precison)
    #输出结果文件地址，要修改
    result.to_csv(params['opath'],index=False)
except Exception as e:
    print(e)
