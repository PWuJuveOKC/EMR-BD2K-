import pandas as pd
import math as m

####################################################################################
################################### Cohort #########################################
####################################################################################
Cohort = pd.read_csv('Processed/Cohort.csv')

## decide variables to keep or remove
Cohort_names = list(Cohort) #303
Cohort_names_keys = [x for x in Cohort_names if 'KEY' in x.upper()]  # 91
Cohort_names_UHC = [x for x in Cohort_names if 'UHC' in x.upper()] #13
Cohort_names_QVI = [x for x in Cohort_names if 'QVI' in x.upper()] #89

Cohort_names_keep = [x for x in Cohort_names if x not in Cohort_names_UHC] #290


## Cohort outcome values count
Cohort_QVI = Cohort.loc[:,Cohort_names_QVI]
Cohort_names_QVI_values_count_list = [Cohort_QVI[outcome].value_counts() for outcome in list(Cohort_names_QVI)]


Cohort = Cohort.loc[:,Cohort_names_keep]
Cohort.dropna(axis=1,thresh=m.ceil(0.3 * len(Cohort)),inplace=True) # (4161,177)
len(Cohort.CurrentPatientKey.unique()) # 2298

Cohort.to_csv('./Processed1/Cohort1.csv',index=None)



####################################################################################
################################### Labs ###########################################
####################################################################################
Lab = pd.read_csv('Processed/LabResults.csv')
Lab_names = list(Lab)
Lab_names_remove = ['VisitKey','VisitNum','AuthorizedByProviderKey', 'AuthProviderNpi', 'AuthProviderName',
                    'AuthProviderSpecialty', 'CollectionDateKey', 'CollectionTimeOfDayKey','EncounterKey',
                    'LabComponentKey', 'LabComponentResultKey','OrderedDateKey', 'OrderedTimeOfDayKey', 'PatientKey',
                    'ProcedureKey','ResultDateKey', 'ResultingLabKey', 'LabName', 'ResultTimeOfDayKey',
                    'LabComponentResultProfileKey']

Lab_names_keep = [x for x in Lab_names if x not in Lab_names_remove]
Lab = Lab.loc[:,Lab_names_keep]
Lab.dropna(axis=0,subset=['Name'],inplace=True) #(136697, 17)

Lab_counts = Lab.Name.value_counts()

print Lab_counts[Lab_counts >= 1000]
Lab_id = Lab.VisitId.unique()
len(Lab_id) #2032
Lab.to_csv('./Processed1/Lab1.csv',index=None)





####################################################################################
################################### Medications ####################################
####################################################################################
Med = pd.read_csv('Processed/Medications.csv')
Med_names = list(Med)
Med_names_remove = ['VisitKey','VisitNum', 'AssociatedDiagnosisComboKey', 'AuthorizedByProviderKey', 'AuthProviderNpi',
                    'AuthProviderName','AuthProviderSpecialty','DepartmentKey', 'DepartmentEpicId', 'DepartmentAbbreviation',
                    'DispenseAsWritten', 'EncounterKey','MedicationKey','Gpi', 'MedicationOrderKey','OrderedByEmployeeKey',
                    'OrderedByProviderKey', 'OrdProviderNpi', 'OrdProviderName','OrdProviderSpecialty', 'OrderedDateKey',
                    'OrderedTimeOfDayKey', 'PatientKey', 'PharmacyKey','PharmacyName']

Med_names_keep = [x for x in Med_names if x not in Med_names_remove]
Med = Med.loc[:,Med_names_keep] # (14084, 27)

Med_counts = Med.PharmaceuticalClass.value_counts()

print Med_counts[Med_counts >= 100]
Med_id = Med.VisitId.unique()
len(Med_id) #961
Med.to_csv('./Processed1/Med1.csv',index=None)


####################################################################################
################################### Diagnosis ######################################
####################################################################################
Diagnosis = pd.read_csv('Processed/Diagnosis.csv')
Diag_names = list(Diagnosis)
Diag_names_remove = ['DiagSeq', 'DiagnosisKey']

Diag_names_keep = [x for x in Diag_names if x not in Diag_names_remove]
Diagnosis = Diagnosis.loc[:,Diag_names_keep] #(12101, 6)

Diag_counts = Diagnosis.DiagCode.value_counts()

print Diag_counts[Diag_counts >= 100]
Diag_id = Diagnosis.VisitId.unique()
len(Diag_id) #3219
Diagnosis.to_csv('./Processed1/Diagnosis1.csv',index=None)



####################################################################################
################################### Flowsheet ######################################
####################################################################################
Flow = pd.read_csv('Processed/Flowsheet.csv')
Flow_names = list(Flow)
Flow_names_remove = ['VisitKey','CosignedByEmployeeKey', 'DateKey','EncounterKey', 'FlowsheetValueKey',
                     'TakenByEmployeeKey', 'FlowsheetRowKey', 'Abbreviation']

Flow_names_keep = [x for x in Flow_names if x not in Flow_names_remove]
Flow = Flow.loc[:,Flow_names_keep] #(808775, 19)

# Flow.dropna(axis=0,subset=['NumericValue'],inplace=True) #(270855, 17)

Flow_counts = Flow.ValueType.value_counts()

print Flow_counts
Flow_id = Flow.VisitId.unique()
len(Flow_id) #2117
Flow.to_csv('./Processed1/Flow1.csv',index=None)

EX1 = Flow[Flow.ValueType == 'Custom List']
EX2 = Flow[Flow.ValueType == 'Numeric Type']
EX3 = Flow[Flow.ValueType == 'String Type']
EX4 = Flow[Flow.ValueType == 'Blood Pressure']
EX5 = Flow[Flow.ValueType == 'Date']
EX6 = Flow[Flow.ValueType == 'Category Type']
EX7 = Flow[Flow.ValueType == 'Temperature']
EX8 = Flow[Flow.ValueType == 'Time']
EX9 = Flow[Flow.ValueType == 'Patient Weight']
EX10 = Flow[Flow.ValueType == 'Patient Height']
EX11 = Flow[Flow.ValueType == 'Weight']
EX12 = Flow[Flow.ValueType == 'Height']

####################################################################################
################################### ProblemList ####################################
####################################################################################
Prob = pd.read_csv('Processed/Problem.csv')
Prob_names = list(Prob)
Prob_names_remove = ['VisitKey','VisitNum', 'AgeKey','DepartmentKey', 'DiagnosisKey','DocumentedByProviderKey',
                     'DocumentedByProviderNpi', 'DocumentedByProviderName', 'DocumentedByProviderSpecialty',
                     'EmergencyDepartmentDiagnosis', 'EncounterKey', 'EndDateKey', 'PatientKey']

Prob_names_keep = [x for x in Prob_names if x not in Prob_names_remove]
Prob = Prob.loc[:,Prob_names_keep] #(16333, 7)


Prob_counts = Prob.DiagnosisCode.value_counts()

print Prob_counts[Prob_counts>=100]
Prob_id = Prob.VisitId.unique()
len(Prob_id) #482
Prob.to_csv('./Processed1/Prob1.csv',index=None)


####################################################################################
################################### Procedure ####################################
####################################################################################
Proc = pd.read_csv('Processed/Procedure.csv')
Proc_names = list(Proc)
Proc_names_remove = ['VisitKey','ProcFinishDatm','SugeonName']

Proc_names_keep = [x for x in Proc_names if x not in Proc_names_remove]
Proc = Proc.loc[:,Proc_names_keep] #(590, 8)

Proc_counts = Proc.SurgeonSpecialty.value_counts()
print Proc_counts

Proc_id = Proc.VisitId.unique()
len(Proc_id) #473
Proc.to_csv('./Processed1/Procedure1.csv',index=None)


####################################################################################
################################### Procedure ####################################
####################################################################################
Roth = pd.read_csv('Processed/Rothman.csv')
Roth_names = list(Roth)
Roth_names_remove = ['VisitKey','VisitNum','chartguid','EpicDeptId', 'mrn', 'EpicProviderId','BUN_AGE', 'Temp_AGE', 'Cardiac_AGE',]

Roth_names_keep = [x for x in Roth_names if x not in Roth_names_remove]
Roth = Roth.loc[:,Roth_names_keep] #(18290, 30)


Roth_id = Roth.VisitId.unique()
len(Roth_id) #376
Roth.to_csv('./Processed1/Roth1.csv',index=None)