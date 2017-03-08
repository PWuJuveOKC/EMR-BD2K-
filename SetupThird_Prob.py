import pandas as pd
import math as m
import numpy as np
import time

####################################################################################
################################### ProbList #######################################
####################################################################################

Prob = pd.read_csv('Processed1/Prob1.csv')
test_count = Prob.DiagnosisCode.value_counts()
test = test_count.index
len(test) #335

Prob_sub = Prob.loc[:,['VisitId','DiagnosisCode']]

Prob_ID = Prob.VisitId.unique() #590


df = Prob_sub.copy()

start_time = time.time()
# df = Lab.copy()
test_count1 = df.DiagnosisCode.value_counts()
test1 = test_count1.index
test1 = list(test1)

ID = df.VisitId.unique()
Final = pd.DataFrame(ID)
Final.columns = ['VisitId']


for item in test1:

    dat = df[df.DiagnosisCode == item]
    dat.reset_index(inplace=True,drop=True)

    dat.is_copy=False
    dat.loc[:,'idx'] = np.array(dat.groupby('VisitId').cumcount())

    dat.drop_duplicates(subset=['VisitId'],keep='last',inplace=True)
    dat.idx = dat.idx + 1
    dat.rename(columns={'idx': item+'_count'},inplace=True)
    dat.drop(labels='DiagnosisCode',axis=1,inplace=True)
    Final = pd.merge(Final,dat,on='VisitId',how='left')

cost = time.time() - start_time
print cost ##14

Final.fillna(value=0,inplace=True)

Final.to_csv('Processed2/Prob_long.csv',index=None)
