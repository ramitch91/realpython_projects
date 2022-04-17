# Entered by the course writer
# from openpyxl import Workbook
#
# workbook = Workbook()
# sheet = workbook.active
#
# sheet["A1"] = "hello"
# sheet["B1"] = "world!"
#
# workbook.save(filename="hello_world.xlsx")

# Entered by me during the class
from openpyxl import Workbook
import os

cwd = os.getcwd()
os.chdir(cwd + "/Data Collection and Storage/Excel Spreadsheets in Python")

workbook = Workbook()
sheet = workbook.active

sheet["A1"] = "hello"
sheet["B1"] = "world!"
sheet["A3"] = "Have a nice day!"

workbook.save(filename="hello_world.xlsx")
