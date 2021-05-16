import os
from time import sleep
import pyodbc
from pathlib import Path
from dotenv import load_dotenv


envPath = Path("utility/Database/a.env")
load_dotenv(dotenv_path=envPath)

server = os.environ.get("SERVER")
database = os.environ.get("DATABASE")
username = os.environ.get("UID")
password = os.environ.get("PSWD")
port = os.environ.get("PORT")
driver = "{ODBC Driver 17 for SQL Server}"


def connect():
    cnxn = pyodbc.connect(
        "DRIVER="
        + driver
        + ";PORT=1433;SERVER="
        + server
        + ";PORT=1443;DATABASE="
        + database
        + ";UID="
        + username
        + ";PWD="
        + password
    )
    cursor = cnxn.cursor()
    return cursor


def exectueQuery(query):
    cursor = connect()
    cursor.execute(query)
    return cursor
