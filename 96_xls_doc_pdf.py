# Workbook
# .xls extension
# Sheets/Worksheets
# Columns & Rows
# Cell

# pip install openpyxl (thirdparty)

import openpyxl
import os

os.chdir('./somefolder/')
workbook = openpyxl.load_workbook('example.xlsx')
type(workbook) # to check if it's a workbook

sheet = worksheet.get_sheet_by_name('Sheet1')
type(workbook) # to check if it's sheet

 namesOfSheetsList = worksheet.get_sheet_by_names()

 cellA1 = sheet['A1'] # gets a cell object

cellA1.value # automatically transforms. example '4/5/2014 13:34' =  datetime.datetime(2014,4,5,13,34,2)
str(cellA1.value) # 4/5/2014 13:34 returns exact text from cell

# you can also use : (to get cells)
cellA1_2 = sheet.cell(row = 1, column = 1)
#cellA1_2 == cellA1



# EDITING SPREADSHEET
import openpyxl , os
wb = openpyxl.Workbook() # creates a new one
wb.get_sheet_names() # ['Sheet']
sheet = wb.get_sheet_name('Sheet')
sheet['A1'] == None  # True

#to save info (just in memory for now)
sheet['A1'] = 42
sheet['A1'] = 'Hello'

os.chdir('./folder') #specify path
wb.save('example.xlsx') #save it with a different filename if you had a previous
# to avoid overwritting

# Add more sheets

sheet2 = wb.create_sheet() 
sheet2.title # Sheet2 (defautl name)
sheet2.title = 'mysheet2'
wb.save('example2.xlsx') # assign name

sheet3 = wb.create_sheet(index = 0, title = 'mythirdsheet') # this creates a new sheet and places it as the first (position) sheet
wb.save('example3.xlsx')


#PDF