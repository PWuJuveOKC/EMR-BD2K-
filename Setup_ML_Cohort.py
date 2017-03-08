import pandas as pd
import math as m
import numpy as np
import time


######################## Read in Cohort and CohortPV and Merge by CurrentKey ##############################
Cohort = pd.read_table('Processed3/HVC_CohortDatm.txt',delimiter='\t', engine='python',
                       header='infer',quotechar=" ") #(6935, 181)

Cohort_names = list(Cohort)

Cohort_QVI_names = [x for x in Cohort_names if ('QVI' in x.upper()) | (x=='VisitId') | (x =='CurrentPatientKey')]

Cohort_QVI = Cohort.loc[:,Cohort_QVI_names]

Cohort_VisitId = Cohort_QVI.VisitId.unique()
Cohort_CurrentKey = Cohort_QVI.CurrentPatientKey.unique() #6459

############################### Only Keep First Record  ######################################

Cohort_QVI.sort_values(by=['CurrentPatientKey','VisitId'],inplace=True)
Cohort_QVI.drop_duplicates(subset=['CurrentPatientKey'],inplace=True,keep='first')



################################ Read in Past Data #############################################
CohortPV_QVI = pd.read_csv('Processed3/CohortPV_QVI.csv')

CohortPV_JoinKey = CohortPV_QVI.loc[:,['VisitId','CurrentPatientKey']]
CohortPV_JoinKey.sort_values(by=['CurrentPatientKey','VisitId'],ascending=[1,1],inplace=True)

CohortPV_CurrentKey = CohortPV_JoinKey.CurrentPatientKey.unique() #2297


test = Cohort_QVI[Cohort_QVI.CurrentPatientKey.isin(CohortPV_CurrentKey)]

Cohort_Join = pd.merge(CohortPV_JoinKey,Cohort_QVI,how='inner',on =['CurrentPatientKey'])

Cohort_Join.rename(columns={'VisitId_x':'VisitId'},inplace=True)
Cohort_Join.to_csv('Processed4/Labels.csv',index=None)



