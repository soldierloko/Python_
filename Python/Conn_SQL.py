
import pyodbc 

#String de Conexão
conn =  pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=DESKTOP-QRGC4CU\SQLEXPRESS;"
    "Database=AdventureWorksDW2017;"
    "Trusted_Connection=yes"
)

#Cria um Cursor Com a conexão
cursor = conn.cursor()

#Executa uma Query
cursor.execute('SELECT TOP (1000) [ProductKey],[ProductAlternateKey] FROM [AdventureWorksDW2017].[dbo].[DimProduct]')


#Percorre a Consulta (Mais valer colocar em um DataFranme)
for row in cursor:
    print(f'row = {row}')

#Fecha a Conexão
conn.close()

