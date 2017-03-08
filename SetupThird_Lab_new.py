import pandas as pd
import math as m
import numpy as np
import time

####################################################################################
################################### Cohort #########################################
####################################################################################
Cohort = pd.read_csv('Processed1/Cohort1.csv')

Lab = pd.read_csv('Processed1/Lab1.csv')
test_count = Lab.Name.value_counts()
test = test_count.index
len(test) #1070

Lab_sub = Lab.loc[:,['VisitId','Name','NumericValue','ReferenceValues','Unit','Value','Flag']]

Lab_ID = Lab.VisitId.unique()

Lab_ID1 = Lab_ID[0:30]
Lab_toy = Lab_sub[Lab_sub.VisitId.isin (Lab_ID1)]


df = Lab_sub.copy()



start_time = time.time()
# df = Lab.copy()
test_count1 = df.Name.value_counts()
test1 = test_count1.index
test1 = list(test1)

ID = df.VisitId.unique()
Final = pd.DataFrame(ID)
Final.columns = ['VisitId']


for item in test1:

    dat = df[df.Name == item]
    dat.reset_index(inplace=True,drop=True)

    dat.is_copy=False
    dat.loc[:,'idx'] = np.array(dat.groupby('VisitId').cumcount())

    # temp = []
    varlist = ['Name','NumericValue','ReferenceValues','Unit','Value','Flag']


    reshape = dat.pivot(index='VisitId',columns='idx')[varlist]

    var_list = list(reshape)
    var_list_new = [item + '_' + x[0] + str(x[1]) for x in var_list]
    reshape.columns = var_list_new
    reshape['VisitId'] = reshape.index
    name_list = [x for x in list(reshape) if 'Name' in x]


    NumericValue_list = [x for x in list(reshape) if 'NumericValue' in x]
    reshape_Numeric= reshape.loc[:,NumericValue_list]

    count_array = reshape_Numeric.count(axis=1)
    mean_array = reshape_Numeric.mean(axis=1)
    std_array = reshape_Numeric.std(axis=1)
    min_array = reshape_Numeric.min(axis=1)
    max_array = reshape_Numeric.max(axis=1)
    reshape.loc[:, item + '_count'] = count_array
    reshape.loc[:, item + '_mean'] = mean_array
    reshape.loc[:, item + '_std'] = std_array
    reshape.loc[:, item + '_min'] = min_array
    reshape.loc[:, item + '_max'] = max_array

    reshape1 = pd.get_dummies(reshape,columns=name_list,drop_first=False)
    Final = pd.merge(Final,reshape1,on='VisitId',how='left')

cost = time.time() - start_time
print cost ##1510



Features = list(Final)

Features_CO2 = [x for x in Features if ('CO2' in x) & ('PCO2' not in x) & ('POC' not in x)]
# Features_Unit = [x for x in Features if ('Unit0' in x)]

Features_remove1 = [x for x in Features if ('Unit' in x) & ('Unit0' not in x)]
Features_remove2 = [x for x in Features if ('ReferenceValues' in x) & ('ReferenceValues0' not in x)]

Features_remove = Features_remove1 + Features_remove2
Features_keep = [x for x in Features if x not in Features_remove]

Final1 = Final.loc[:,Features_keep]

Final1.to_csv('Processed2/Lab_long_new.csv',index=None)