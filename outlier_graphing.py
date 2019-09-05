# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 19:03:20 2018

@author: smoor
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# creating a dataframe to read in our datasets

#  318 MB
df = pd.read_csv('deputies_dataset.csv')

#plt.title('Receipt Price Grouped by Receipt Description')
#plt.scatter(df['receipt_value'],df['receipt_description'])
#plt.show()

#plt.savefig('scatter.png')
'''
# Create dataframes based on groups
grouped_df = dep_df.groupby('receipt_description')    
df_arr = [grouped_df.get_group(df) for df in grouped_df.groups]

for df in df_arr:
	response = input('Would you like to see ' + df['receipt_description'].iloc[0] + '? ')
	if (response.lower() == 'y'):
		plt.title(df['receipt_description'].iloc[0])
		plt.scatter(df['deputy_id'],df['receipt_value'])
		plt.show()

'''

grouped_df = df.groupby('receipt_description')    
df_arr = [grouped_df.get_group(df) for df in grouped_df.groups]
counter = 0

for df in df_arr:
    #response = input('Would you like to see ' + df['receipt_description'].iloc[0] + '? ')
    #if (response.lower() == 'y'):
    plt.title(df['receipt_description'].iloc[0])
    plt.boxplot(df['receipt_value'])
    filename = 'outlier' + str(counter) + '.png'
    plt.savefig(filename)
    counter += 1

