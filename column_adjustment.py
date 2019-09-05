# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 07:24:42 2018

@author: smoor

@description: Adjusts column width in an excel file
"""

import openpyxl

def adjust_column(file):    
    wb = openpyxl.load_workbook(filename = file)        
    worksheet = wb.active
    
    for col in worksheet.columns:
         max_length = 0
         column = col[0].column # Get the column name
         for cell in col:
             try: # Necessary to avoid error on empty cells
                 if len(str(cell.value)) > max_length:
                     max_length = len(cell.value)
             except:
                 pass
         adjusted_width = (max_length + 2) * 1.2
         worksheet.column_dimensions[column].width = adjusted_width
         
    wb.save(file)