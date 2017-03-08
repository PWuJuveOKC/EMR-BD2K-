import pandas as pd
import math as m
import numpy as np
import time

####################################################################################
################################### Lab #########################################
####################################################################################

Lab = pd.read_csv('Processed1/Lab1.csv')
test_count = Lab.Name.value_counts()
test = test_count.index
len(test) #1070

Lab_sub = Lab.loc[:,['VisitId','Name','NumericValue','ReferenceValues','Unit','Value','Flag']]

Lab_ID = Lab.VisitId.unique()

Lab_ID1 = Lab_ID[0:30]
Lab_toy = Lab_sub[Lab_sub.VisitId.isin (Lab_ID1)]


df = Lab_toy.copy()



start_time = time.time()
# df = Lab.copy()
test_count1 = Lab_toy.Name.value_counts()
test1 = test_count1.index
test1 = list(test1)

ID = df.VisitId.unique()
Final = pd.DataFrame(ID)
Final.columns = ['VisitId']

for item in test1:

    dat = df[df.Name == item]
    dat.reset_index(inplace=True)

    dat.is_copy=False
    dat.loc[:,'idx'] = np.array(dat.groupby('VisitId').cumcount())

    # temp = []
    varlist = ['Name','NumericValue','ReferenceValues','Unit','Value','Flag']
    # for var in varlist:
    #     dat['temp_idx'] = dat.idx.astype(str) + '_' + var
    #     temp.append(dat.pivot(index='VisitId',columns='temp_idx',values=var))

    # reshape = pd.concat(temp,axis=1)
    reshape = dat.pivot(index='VisitId',columns='idx')[varlist]

    var_list = list(reshape)
    var_list_new = [item + '_' + x[0] + str(x[1]) for x in var_list]
    reshape.columns = var_list_new
    reshape['VisitId'] = reshape.index
    name_list = [x for x in list(reshape) if 'Name' in x]
    reshape1 = pd.get_dummies(reshape,columns=name_list,drop_first=False)
    Final = pd.merge(Final,reshape1,on='VisitId',how='left')

cost = time.time() - start_time
print cost