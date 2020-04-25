import pyodbc 

conn =  pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=DESKTOP-QRGC4CU\SQLEXPRESS;"
    "Database=AdventureWorksDW2017;"
    "Trusted_Connection=yes"
)
cursor = conn.cursor()
cursor.execute('SELECT TOP (1000) [ProductKey],[ProductAlternateKey] FROM [AdventureWorksDW2017].[dbo].[DimProduct]')

for row in cursor:
    print(f'row = {row}')

conn.close()

