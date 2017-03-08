import pandas as pd
import math as m
import numpy as np
import time

####################################################################################
################################### Med #########################################
####################################################################################

Med = pd.read_csv('Processed1/Med1.csv')
test_count = Med.PharmaceuticalClass.value_counts()
test = test_count.index
len(test) #266

Med_sub = Med.loc[:,['VisitId','PharmaceuticalClass']]

Med_ID = Med.VisitId.unique() #1207
#
# Med_ID1 = Med_ID[0:8]
# Med_toy = Med_sub[Med_sub.VisitId.isin (Med_ID1)]
#
# df = Med_toy.copy()

df = Med_sub.copy()

start_time = time.time()
# df = Lab.copy()
test_count1 = df.PharmaceuticalClass.value_counts()
test1 = test_count1.index
test1 = list(test1)

ID = df.VisitId.unique()
Final = pd.DataFrame(ID)
Final.columns = ['VisitId']


for item in test1:

    dat = df[df.PharmaceuticalClass == item]
    dat.reset_index(inplace=True,drop=True)

    dat.is_copy=False
    dat.loc[:,'idx'] = np.array(dat.groupby('VisitId').cumcount())

    dat.drop_duplicates(subset=['VisitId'],keep='last',inplace=True)
    dat.idx = dat.idx + 1
    dat.rename(columns={'idx': item+'_count'},inplace=True)
    dat.drop(labels='PharmaceuticalClass',axis=1,inplace=True)
    Final = pd.merge(Final,dat,on='VisitId',how='left')

cost = time.time() - start_time
print cost ##10

Final.fillna(value=0,inplace=True)

Final.to_csv('Processed2/Med_long.csv',index=None)
