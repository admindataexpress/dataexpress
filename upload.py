# This is the Data Express main.py file
# Install the corresponding libraries.

# To run this script, you will need to install the google cloud sdk command line tool: https://cloud.google.com/sdk/gcloud
# Before using this script you will need to run the following command in the command line 'gcloud auth login' to be able to access you Big Query projects.

# os is a library that allows us to run command line commands from python.

import os #https://docs.python.org/3/library/os.html

# This function will upload the csv file generated in the main.py function to BigQuery.
def upload_data():
    # Set the project ID
    os.system("gcloud config set project ###") # This command sets the project ID. You will need to replace the ### with your own project ID.

    # Load the CSV file into a BigQuery table
    os.system("bq load --replace --autodetect dataset.table_name #/###/###.csv") # This command loads the csv file into a BigQuery table. You will need to replace the dataset.table_name with your own dataset name and table, also change the path to the csv file.
    # bq is a command for Big Query, '--replace' will create or replace an existing table, '--autodetect' will automatically detect the schema of the csv file, and the last part is the path to the csv file.
    # bq documentation: https://cloud.google.com/bigquery/docs/batch-loading-data#appending_to_or_overwriting_a_table
    print('Upload done') # Test print statement.
    
