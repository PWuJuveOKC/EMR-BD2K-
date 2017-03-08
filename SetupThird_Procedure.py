import pandas as pd
import math as m
import numpy as np
import time

####################################################################################
################################### Procedure ######################################
####################################################################################

Proc = pd.read_csv('Processed1/Procedure1.csv')
test_count = Proc.SurgeonSpecialty.value_counts()
test = test_count.index
len(test) #21

Proc_sub = Proc.loc[:,['VisitId','SurgeonSpecialty']]

Proc_ID = Proc.VisitId.unique() #585


df = Proc_sub.copy()

start_time = time.time()
# df = Lab.copy()
test_count1 = df.SurgeonSpecialty.value_counts()
test1 = test_count1.index
test1 = list(test1)

ID = df.VisitId.unique()
Final = pd.DataFrame(ID)
Final.columns = ['VisitId']


for item in test1:

    dat = df[df.SurgeonSpecialty == item]
    dat.reset_index(inplace=True,drop=True)

    dat.is_copy=False
    dat.loc[:,'idx'] = np.array(dat.groupby('VisitId').cumcount())

    dat.drop_duplicates(subset=['VisitId'],keep='last',inplace=True)
    dat.idx = dat.idx + 1
    dat.rename(columns={'idx': item+'_count'},inplace=True)
    dat.drop(labels='SurgeonSpecialty',axis=1,inplace=True)
    Final = pd.merge(Final,dat,on='VisitId',how='left')

cost = time.time() - start_time
print cost ##0.2

Final.fillna(value=0,inplace=True)

Final.to_csv('Processed2/Proc_long.csv',index=None)
