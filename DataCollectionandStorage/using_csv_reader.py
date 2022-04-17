import csv
import os

cwd = os.getcwd()
os.chdir(cwd + "/Data Collection and Storage")

with open("employee_birthday.csv", encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        print(row)
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(
                f"\t{row[0]} works in the {row[1]} department, and was born in {row[2]}."
            )
            line_count += 1
    print(f"Processed {line_count} lines.")
