import pandas as pd
import math as m
import numpy as np
import time

####################################################################################
################################### Roth #########################################
####################################################################################

Roth = pd.read_csv('Processed1/Roth1.csv')
Roth.timestamp = pd.to_datetime(Roth.timestamp)

Roth.sort_values(by=['VisitId','timestamp'],inplace=True)
Roth.reset_index(inplace=True,drop=True)

Roth_ID = Roth.VisitId.unique()
len(Roth_ID) #463

Roth.drop(axis=1,labels=['valid'],inplace=True)



# Roth_ID1 = Roth_ID[0:30]
# Roth_toy = Roth[Roth.VisitId.isin (Roth_ID1)]
#
#
# df = Roth_toy.copy()

df = Roth.copy()



start_time = time.time()
# df = Lab.copy()


ID = df.VisitId.unique()
Final = pd.DataFrame(ID)
Final.columns = ['VisitId']

test1 = list(Roth)[2:]

for item in test1:

    dat = df.loc[:,['VisitId',item]]

    dat.is_copy=False
    dat.loc[:,'idx'] = np.array(dat.groupby('VisitId').cumcount())

    reshape = dat.pivot(index='VisitId',columns='idx')

    var_list = list(reshape)
    var_list_new = [item + '_' + x[0] + str(x[1]) for x in var_list]
    reshape.columns = var_list_new

    count_array = reshape.count(axis=1)
    mean_array = reshape.mean(axis=1)
    std_array = reshape.std(axis=1)
    min_array = reshape.min(axis=1)
    max_array = reshape.max(axis=1)
    reshape.loc[:,item + '_count' ] = count_array
    reshape.loc[:,item + '_mean' ] = mean_array
    reshape.loc[:,item + '_std' ] = std_array
    reshape.loc[:,item + '_min' ] = min_array
    reshape.loc[:,item + '_max' ] = max_array

    reshape['VisitId'] = reshape.index
    Final = pd.merge(Final,reshape,on='VisitId',how='left')

cost = time.time() - start_time
print cost ##3

Final.to_csv('Processed2/Roth_long.csv',index=None)