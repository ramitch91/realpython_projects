import csv
import os

cwd = os.getcwd()
os.chdir(cwd + "/Data Collection and Storage")

with open("employee_file_1.csv", mode="w") as employee_file:
    employee_writer = csv.writer(
        employee_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL
    )

    employee_writer.writerow(["John Smith", "Accounting", "November"])
    employee_writer.writerow(["Erica Meyers", "IT", "March"])