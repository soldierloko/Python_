import pyodbc 

conn =  pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=DESKTOP-QRGC4CU\SQLEXPRESS;"
    "Database=AdventureWorksDW2017;"
    "Trusted_Connection=yes"
)

row = cursor.fetchone
                        
while row:
    print(row[0])
    row = cursor.fetchone()

#cursor.execute('SELECT TOP (1000) [ProductKey],[ProductAlternateKey] FROM [AdventureWorksDW2017].[dbo].[DimProduct]')
#row = cursor.fetchone()
#while row:
 #   print(row[0])
  #  row = cursor.fetchone()

  conn.close()

