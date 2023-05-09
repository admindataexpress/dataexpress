# This is the Data Express main.py file
# Install the corresponding libraries.


# pyodbc is for connecting to the database. You will need to install the appropiate driver for your database: https://github.com/mkleehammer/pyodbc/wiki.
# pandas is used to transform the fetched query results and export as a .csv
# time is used to set up a time.sleep() function to allow the script to run every (x) amount of time.

# FYI: There are other libraries imported in the upload.py file.

import pyodbc #https://pypi.org/project/pyodbc/
import pandas as pd #https://pandas.pydata.org/
import time #https://docs.python.org/3/library/time.html
from upload import upload_data

# This function makes the connection to the database, fetches the data, transforms it, and exports it to a .csv file.
def connect():
    cnxn = None 
    try: #
        print('Connecting to the database...') 
        cnxn = pyodbc.connect('DRIVER={###};SERVER=###;DATABASE=###;UID=###;PWD=###') # This is the connection string. You will need to replace the ### with your own credentials.
        crsr = cnxn.cursor() # Documentation: https://github.com/mkleehammer/pyodbc/wiki/Cursor. 
        crsr.execute("SELECT ### FROM ###;") # This is the query that will be executed. You will need to replace the ### with your own query.
        print('Query executed.')
        rows = crsr.fetchall() # Fetches all the rows from the query as a list of tuples.
        print('Query results fetched.')
        csv_data = [",".join(map(str, row)) for row in rows] # Transforms the list of tuples into a list of strings, each string representing a row.
        print('List of tuples transformed into list of strings.')
        split_data = [row.split(",") for row in csv_data] # Transforms the list of strings into a list of lists, each list representing a row, each column separated by a comma.
        print('List of strings transformed into list of lists.')
        df = pd.DataFrame(split_data, columns=['###', '###']) # Replace '###' with the corresponding column names.
        print('List of lists transformed into dataframe.')
        df.to_csv("#/###/###.csv", index=False) 
        print('OUTPUT FILE GENERATED')
        crsr.close()

    except(Exception, pyodbc.Error) as error: # Exception handling by pyodbc: https://github.com/mkleehammer/pyodbc/wiki/Exceptions.
        print(error)

    finally: 
        if cnxn is not None:
            cnxn.close()
            print('Database connection terminated.')
            print('Initiating upload to BigQuery.')
            upload_data() # Calls the function from the upload.py file.

while True:
    print("Los datos seran actualizados cada 5 min.")
    connect()
    time.sleep(300) # 300 seconds (5 minutes). Change this as needed.
