import os
import mysql.connector
from mysql.connector import Error


cwd = os.getcwd()
os.chdir(cwd + "/Data Collection and Storage/Introduction to Python SQL Libraries")


def create_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name, user=user_name, password=user_password
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occuured")

    return connection


connection = create_connection("localhost", "root", "")
