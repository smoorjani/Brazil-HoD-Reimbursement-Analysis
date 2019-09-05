import numpy as np
import pandas as pd

# Removes most unnecessary data

# Reading in our dataset (318 MB)
df = pd.read_csv('deputies_dataset.csv')
# Gets rid of columns like time, receipt SSN, etc which are
# largely unnecessary for our project
df.drop(df.columns[[0,1,2,6,8]],axis=1,inplace=True)
# Outputs to new CSV file (138 MB)
df.to_csv('minimized.csv',index=False)



