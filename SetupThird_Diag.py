import pandas as pd
import math as m
import numpy as np
import time

####################################################################################
################################### Lab #########################################
####################################################################################

Diag = pd.read_csv('Processed1/Diagnosis1.csv')
test_count = Diag.DiagCode.value_counts()
test = test_count.index
len(test) #1289

Diag_sub = Diag.loc[:,['VisitId','DiagCode']]

Diag_ID = Diag.VisitId.unique() #3908


df = Diag_sub.copy()

start_time = time.time()
# df = Lab.copy()
test_count1 = df.DiagCode.value_counts()
test1 = test_count1.index
test1 = list(test1)

ID = df.VisitId.unique()
Final = pd.DataFrame(ID)
Final.columns = ['VisitId']


for item in test1:

    dat = df[df.DiagCode == item]
    dat.reset_index(inplace=True,drop=True)

    dat.is_copy=False
    dat.loc[:,'idx'] = np.array(dat.groupby('VisitId').cumcount())

    dat.drop_duplicates(subset=['VisitId'],keep='last',inplace=True)
    dat.idx = dat.idx + 1
    dat.rename(columns={'idx': item+'_count'},inplace=True)
    dat.drop(labels='DiagCode',axis=1,inplace=True)
    Final = pd.merge(Final,dat,on='VisitId',how='left')

cost = time.time() - start_time
print cost ##286

Final.fillna(value=0,inplace=True)

Final.to_csv('Processed2/Diag_long.csv',index=None)
