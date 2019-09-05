import numpy as np
import pandas as pd
from scipy.stats import iqr

# This program finds outliers in a given dataset

df = pd.read_csv('minimized.csv')

grouped_df = df.groupby('receipt_description')
# Grouping dataframes into a list of dataframes based on receipt_value
df_arr = [grouped_df.get_group(df) for df in grouped_df.groups]

# Creating a dataframe to hold all statistical values
df_groups = pd.DataFrame(index=df['receipt_description'].unique(),columns=['iqr','first','third','min_val','max_val'])
outliers = pd.DataFrame(columns=df.columns)

for df in df_arr:
    # Interquartile Range
    df_groups.at[str(list(df.iloc[1])[3]),'iqr'] = iqr(df['receipt_value'])
    # First Quartile
    df_groups.at[str(list(df.iloc[1])[3]),'first'] = np.percentile(df['receipt_value'],25)
    # Third Quartile
    df_groups.at[str(list(df.iloc[1])[3]),'third'] = np.percentile(df['receipt_value'],75)
    # Min Val (Lowest number a point can be without being an outlier)
    df_groups.at[str(list(df.iloc[1])[3]),'min_val'] = df_groups.at[str(list(df.iloc[1])[3]),'first'] - (1.5 * df_groups.at[str(list(df.iloc[1])[3]),'iqr'])
    # Max Val (Highest number a point can be without being an outlier)
    df_groups.at[str(list(df.iloc[1])[3]),'max_val'] = df_groups.at[str(list(df.iloc[1])[3]),'third'] + (1.5 * df_groups.at[str(list(df.iloc[1])[3]),'iqr'])

    min_val = df_groups.at[str(list(df.iloc[1])[3]),'min_val']
    max_val = df_groups.at[str(list(df.iloc[1])[3]),'max_val']
    # We don't really care about outliers that are below, but we might as well check them for now in case of negatives
    #print(df.loc[df['receipt_value'].sort_values() < min_val])
    # Appending all the outliers to our outliers dataframe
    outliers = pd.concat([outliers,df.loc[df['receipt_value'].sort_values() > max_val]])

df_groups.to_csv('stats.csv')
outliers.to_csv('outliers.csv')
