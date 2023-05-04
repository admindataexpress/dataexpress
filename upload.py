import os #https://docs.python.org/3/library/os.html
def upload_data():

    os.system('bq load --replace --source_format=CSV --skip_leading_rows=1 --schema="BusinessEntityName:STRING, DocFolio:INTEGER, DocumentID:INTEGER, DateDocument:DATE, DayHour:TIMESTAMP, SubTotal:FLOAT, Total:FLOAT" facturacion.customer_invoice C:/Users/dario/Desktop/python/customerinvoice.csv')

    print('Upload done')
