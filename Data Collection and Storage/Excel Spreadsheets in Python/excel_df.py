from dataclasses import dataclass
import os
import pandas as pd
from openpyxl import load_workbook
from mapping import REVIEW_ID

cwd = os.getcwd()
os.chdir(cwd + "/Data Collection and Storage/Excel Spreadsheets in Python")

workbook = load_workbook(filename="sample.xlsx")
sheet = workbook.active

data = sheet.values

# set the first row as te headers
cols = next(data)
data = list(data)

# set the index
idx = [row[REVIEW_ID] for row in data]

df = pd.DataFrame(data, index=idx, columns=cols)

print(df.head())
