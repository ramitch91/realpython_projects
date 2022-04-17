import os
from openpyxl import load_workbook
from openpyxl.drawing.image import Image

cwd = os.getcwd()
os.chdir(cwd + "/Data Collection and Storage/Excel Spreadsheets in Python")

workbook = load_workbook("hello_world.xlsx")
sheet = workbook.active

logo = Image("rp.png")
logo.height = 150
logo.width = 150

sheet.add_image(logo, "A3")
workbook.save(filename="hello_world_logo.xlsx")
