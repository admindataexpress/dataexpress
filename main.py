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

# This is the function that connects to the database, fetches the data, transforms it, and exports it to a .csv file.
def connect():
    cnxn = None # We set the connection to None so that we can close it later.
    try: # Try some code...
        print('Connecting to the database...') # This is just a print statement to let us know that the script is running.
        cnxn = pyodbc.connect('DRIVER={###};SERVER=###;DATABASE=###;UID=###;PWD=###') # This is the connection string. You will need to replace the ### with your own credentials.
        crsr = cnxn.cursor() # This is the cursor that will be used to execute the query: https://github.com/mkleehammer/pyodbc/wiki/Cursor. 
        crsr.execute("SELECT ### FROM ###;") # This is the query that will be executed. You will need to replace the ### with your own query.
        print('Query executed.') # Test print statement.
        rows = crsr.fetchall() # This fetches all the rows from the query (without the column names).
        # the 'rows' variable is a list of tuples. Each tuple is a row from the query results.
        print('Query results fetched.') # Test print statement.
        csv_data = [",".join(map(str, row)) for row in rows] # This transforms the query results into a list of strings, each string representing a row.
        print('List of tuples transformed into list of strings.')
        split_data = [row.split(",") for row in csv_data] # This transforms the list of strings into a list of lists, each list representing a row, each column separated by a comma.
        print('List of strings transformed into list of lists.')
        df = pd.DataFrame(split_data, columns=['###', '###']) # Here we use pandas to turn the list of lists into a dataframe (add as many column names separated by commas as needed).
        print('List of lists transformed into dataframe.')
        df.to_csv("#/###/###.csv", index=False) # Here we use pandas to export the dataframe to a csv file, you will need to replace the ### with your own path.
        print('OUTPUT FILE GENERATED') # Test print statement.
        crsr.close() # This closes the cursor.

    # This exception is only run if needed...
    except(Exception, pyodbc.Error) as error: # This is the exception handling given by pyodbc: https://github.com/mkleehammer/pyodbc/wiki/Exceptions.
        print(error)

    finally: # This finally statement always runs...
        if cnxn is not None: # This runs if the connection is not 'None'.
            cnxn.close() # This closes the connection.
            print('Database connection terminated.') # Test print statement.
            print('Initiating upload to BigQuery.') # Test print statement.
            upload_data() # This calls the function from the upload.py file.

while True: # This while loop allows the script to run every (x) amount of time.
    print("Los datos seran actualizados cada 5 min.")
    
    connect() # This runs the connect() function declared in this file (main.py).

    time.sleep(300) # Default is 300 seconds (5 minutes). You can change this to whatever you want.