import pandas as pd
import math as m
import numpy as np
import time


Diag = pd.read_csv('Processed2/Diag_long.csv') #(3908,1290)

Med = pd.read_csv('Processed2/Med_long.csv') #(1207, 267)

Roth = pd.read_csv('Processed2/Roth_long.csv') #(463, 21142)

Problem = pd.read_csv('Processed2/Prob_long.csv') #(590, 336)

Procedure = pd.read_csv('Processed2/Proc_long.csv') #(585, 22)

Lab = pd.read_csv('Processed2/Lab_long_new.csv') #(2032, 30939)

CohortPV = pd.read_csv('Processed1/Cohort1.csv') #(4161, 177)



######  Merge the Data First #############
##########################################


DFs = [CohortPV, Lab, Procedure, Problem, Roth, Med, Diag]

DF_Merge = reduce(lambda left,right: pd.merge(left,right,how='left',on='VisitId'),DFs)

DF_Merge.shape #(4161, 54167)

# start = time.time()
# DF_Merge.to_csv('Processed3/Merge_temp.csv',index=None)
# print (time.time() - start) #2510s


######  Toss some messy information ######
##########################################

########### Imputation    ################
############ Impute using Median #########


#### CohortPV: Only Keep QVI Vars
CohortPV_names = list(CohortPV) #177
CohortPV_names_QVI = [x for x in CohortPV_names if 'QVI' in x.upper()]#88
CohortPV_keep = [x for x in CohortPV_names if (x == 'VisitId') | (x == 'CurrentPatientKey') |(x in CohortPV_names_QVI)]
CohortPV1 = CohortPV.loc[:,CohortPV_keep]
CohortPV2 = CohortPV1.select_dtypes(exclude=['object']) ## keep only numeric variables
CohortPV2 = CohortPV2.dropna(axis=1,thresh=0.7)
CohortPV_QVI = CohortPV2.fillna(CohortPV2.median())
CohortPV_QVI.to_csv('Processed3/CohortPV_QVI.csv',index=None)
del CohortPV_QVI['CurrentPatientKey']

CohortPV_QVI = CohortPV_QVI.drop_duplicates(subset='VisitId',keep='first')

VisitId = CohortPV_QVI.VisitId.unique() #4159

Base = pd.DataFrame(VisitId)
Base.columns = ['VisitId']

#### Diagnosis:
Diag1 = Diag.fillna(Diag.median())
Diag2 = pd.merge(Base,Diag1,on='VisitId',how='left')
Diag2 = Diag2.fillna(0)

#### Medications:
Med1 = Med.fillna(Med.median())
Med2 = pd.merge(Base,Med1,on='VisitId',how='left')
Med2 = Med2.fillna(0)


#### Procedures:
Procedure1 = Procedure.fillna(Procedure.median())
Procedure2 = pd.merge(Base,Procedure1,on='VisitId',how='left')
Procedure2 = Procedure2.fillna(0)



# Not used at this moment
# #### Problems:
# Problem1 = Problem.fillna(Problem.median())
#
# #### Rothman:
# Roth1 = Roth.dropna(axis=1,thresh=0.7)
# Roth1 = Roth1.fillna(Roth1.median())


### Lab: Only keep numeric vars
Lab1 = Lab.select_dtypes(exclude=['object']) #(2032, 22106)
Lab1 = Lab1.dropna(axis=1,thresh=0.7) #(2032, 17408)
Lab1 = Lab1.fillna(Lab1.median())


DFs_new = [CohortPV_QVI, Lab1, Procedure2, Med2, Diag2]
DF_Merge_inner = reduce(lambda left,right: pd.merge(left,right,how='inner',on='VisitId'),DFs_new)
DF_Merge_inner.shape #(2032, 19072)


############################## Dump the Inputs to a temp file ########################
start = time.time()
DF_Merge_inner.to_csv('Processed3/Merge_inner_temp.csv',index=None)
print (time.time() - start) #98s