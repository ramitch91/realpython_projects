import csv
import os

cwd = os.getcwd()
os.chdir(cwd + "/Data Collection and Storage")

with open("employee_file_2.csv", mode="w") as employee_file:
    employee_writer = csv.writer(
        employee_file,
        delimiter=",",
        quotechar='"',
        quoting=csv.QUOTE_NONE,
        escapechar="|",
    )

    employee_writer.writerow(["Smith, John", "Accounting", "November"])
    employee_writer.writerow(["Meyers, Ericas", "IT", "March"])
