import os
import sqlite3
from sqlite3 import Error

cwd = os.getcwd()
os.chdir(cwd + "/Data Collection and Storage/Introduction to Python SQL Libraries")


def create_connection(path):
    """creates a connection ot a SQLite DB"""
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connectioin to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


connection = create_connection("sm_app.sqlite")
