import pyodbc

def retornar_conexao_sql():
    server = 'DESKTOP-QRGC4CU\SQLEXPRESS'
    database = 'AdventureWorksDW2017'
    string_conexao = 'Driver={SQL Server Native Client 11.0};Server='+server+';Database='+database+';Trusted_connection=yes;'
    conexao = pyodbc.connect(string_conexao)
    return conexao