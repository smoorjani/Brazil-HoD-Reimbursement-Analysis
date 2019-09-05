# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 07:24:42 2018

@author: smoor

@description: Renders pie chart of percent of money spent on each receipt description
"""

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import pygal

df = pd.read_csv('results.csv')


total_money = df['total_value'].sum() 
df['percent_total'] = list(map(lambda n: round(n, 2),list((100*df['total_value']/total_money))))

pie_chart = pygal.Pie()
pie_chart.title = 'Money spent on different areas (%)'

for receipt in df['receipt_description']:
	pie_chart.add(receipt,df[df['receipt_description'] == receipt]['percent_total'])

pie_chart.render_to_file('pchart.svg')


#df.to_csv('percent_total.csv')

'''
Matplotlib implimentation

plt.figure(figsize=(16,8))
ax1 = plt.subplot(121,aspect='equal')
df.plot(kind='pie',y='percent_total',ax=ax1,labels=df['receipt_description'],fontsize=8,legend=False)

plt.show()

'''