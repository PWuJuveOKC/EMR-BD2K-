import pandas as pd



Cohort = pd.read_table('/data/Projects/YNHH/qvi/data/PastVisit/HVC_CohortPV.txt',delimiter="\|\|",engine='python',
                       header='infer',quotechar=" ")  # (4161,303)

LabResults = pd.read_table('/data/Projects/YNHH/qvi/data/PastVisit/HVC_LabResultsPV.txt',delimiter="\|\|",engine='python',
                           header='infer',quotechar=" ") # (138826, 37)

ProcedureDetails = pd.read_table('/data/Projects/YNHH/qvi/data/PastVisit/HVC_ProcedureDetailsPV.txt',delimiter="\|\|",engine='python',
                                 header='infer',quotechar=" ") #(731, 11)

Diagnosis= pd.read_table('/data/Projects/YNHH/qvi/data/PastVisit/HVC_DiagnosisPV.txt',delimiter="\|\|",engine='python',
                         header='infer',quotechar=" ")  #(14899, 8)

Medications = pd.read_table('/data/Projects/YNHH/qvi/data/PastVisit/HVC_MedicationsPV.txt',delimiter="\|\|",engine='python',
                            header='infer',quotechar=" ") #(17884, 52)

RothmanHealthscore = pd.read_table('/data/Projects/YNHH/qvi/data/PastVisit/RothmanHealthscorePV.txt',delimiter="\|\|",engine='python',
                                   header='infer',quotechar=" ") #(22883, 39)

Flowsheet = pd.read_table('/data/Projects/YNHH/qvi/data/PastVisit/HVC_FlowsheetPV.txt',delimiter="\|\|",engine='python',
                          header='infer',quotechar=" ") #(1043259, 26)

ProblemList = pd.read_table('/data/Projects/YNHH/qvi/data/PastVisit/HVC_ProblemListPV.txt',delimiter="\|\|",engine='python',
                            header='infer',quotechar=" ") #(16485, 20)


####################  Unique ID Check ###########################
Cohort_ID = Cohort.VisitId.unique()
len(Cohort_ID)  #4159

################ Note: Two VisitId are duplicated:
##############  4000004215099    4000004194748
####################################################


Cohort_CurrentKey = Cohort.CurrentPatientKey.unique()
len(Cohort_CurrentKey) #2298

Lab_ID = LabResults.Visitid.unique()
len(Lab_ID)  #4159

Procedure_ID = ProcedureDetails.VisitId.unique()
len(Procedure_ID)  #585

Medications_ID = Medications.Visitid.unique()
len(Medications_ID)  #1207

Diagnosis_ID = Diagnosis.VisitId.unique()
len(Diagnosis_ID) #3908

Rothman_ID = RothmanHealthscore.Visitid.unique()
len(Rothman_ID) #463

Flow_ID = Flowsheet.Visitid.unique()
len(Flow_ID) #2752

ProblemList_ID = ProblemList.Visitid.unique()
len(ProblemList_ID) #590



########################## Sort and Save as CSV #########################
Cohort.sort_values(by='VisitId',ascending=True,inplace=True)
Cohort.to_csv('./Processed/Cohort.csv',index=None)

LabResults.rename(columns={'Visitid':"VisitId"},inplace=True)
LabResults.sort_values(by='VisitId',ascending=True,inplace=True)
LabResults.to_csv('./Processed/LabResults.csv',index=None)

ProcedureDetails.sort_values(by='VisitId',ascending=True,inplace=True)
ProcedureDetails.to_csv('./Processed/Procedure.csv',index=None)

Medications.rename(columns={'Visitid':"VisitId"},inplace=True)
Medications.sort_values(by='VisitId',ascending=True,inplace=True)
Medications.to_csv('./Processed/Medications.csv',index=None)

Diagnosis.sort_values(by='VisitId',ascending=True,inplace=True)
Diagnosis.to_csv('./Processed/Diagnosis.csv',index=None)

RothmanHealthscore.rename(columns={'Visitid':"VisitId"},inplace=True)
RothmanHealthscore.sort_values(by='VisitId',ascending=True,inplace=True)
RothmanHealthscore.to_csv('./Processed/Rothman.csv',index=None)

Flowsheet.rename(columns={'Visitid':"VisitId"},inplace=True)
Flowsheet.sort_values(by='VisitId',ascending=True,inplace=True)
Flowsheet.to_csv('./Processed/Flowsheet.csv',index=None)

ProblemList.rename(columns={'Visitid':"VisitId"},inplace=True)
ProblemList.sort_values(by='VisitId',ascending=True,inplace=True)
ProblemList.to_csv('./Processed/Problem.csv',index=None)