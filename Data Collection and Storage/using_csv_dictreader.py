import csv
import os

cwd = os.getcwd()
os.chdir(cwd + "/Data Collection and Storage")

with open("employee_birthday.csv") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(
            f'\t{row["name"]} works in the {row["department"]}, and born in {row["birthday month"]}'
        )
        line_count += 1
    print(f"Processed {line_count} lines.")
