""" Script to show how to read and write csv files with Pandas."""

import os

import pandas as pd


cwd = os.getcwd()
os.chdir(cwd + "/Data Collection and Storage")

df = pd.read_csv(
    "hrdata.csv",
    index_col="Employee",
    parse_dates=["Hired"],
    header=0,
    names=["Employee", "Hired", "Salary", "Sick Days"],
)

df.loc["Jane Doe"] = ["2021-07-01", "50000", "0"]
df.to_csv("hrdata_modified.csv")

print(df)
