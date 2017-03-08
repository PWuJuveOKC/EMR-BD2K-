import pandas as pd
import math as m
import numpy as np
import time


InputDF = pd.read_csv('Processed3/Merge_inner_temp.csv') #(2032, 19072)

np.any(np.isnan(InputDF)) #False

# InputDF1 = InputDF.apply(pd.to_numeric,errors='coerce')
# InputDF1 = InputDF1.fillna(InputDF1.median())

InputDF.to_csv('Processed4/Input.csv',index=None)





