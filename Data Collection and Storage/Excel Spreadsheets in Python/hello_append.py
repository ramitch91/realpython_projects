import os

from openpyxl import load_workbook

cwd = os.getcwd()
os.chdir(cwd + "/Data Collection and Storage/Excel Spreadsheets in Python")

workbook = load_workbook("hello_world.xlsx")
sheet = workbook.active

sheet["C1"] = "writing!"

workbook.save(filename="hello_world_append.xlsx")
