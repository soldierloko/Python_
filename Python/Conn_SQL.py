# Importa as Bibliotecas
import pandas as pd
import pyodbc

# Biblioteca Personal Funções
import func_py as fp

# Chama a Função de conexão ao SQL
conn = fp.retornar_conexao_sql()

# Armazena a Consulta
sql = 'SELECT TOP (1000) [ProductKey],[ProductAlternateKey] FROM [AdventureWorksDW2017].[dbo].[DimProduct]'

# Executa a Consulta  
sql_query = pd.read_sql(sql,conn)

# Armazena a Consulta no DF (Precisa nomear os campos e colocar quantos campos tem a conmsulta - (index))
df = pd.DataFrame(sql_query,columns = ['ProductKey','ProductAlternateKey'])

# Exibe a consulta
print(df)


