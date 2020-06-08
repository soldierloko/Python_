import func_py as fp
sql = 'SELECT TOP (1000) [ProductKey],[ProductAlternateKey] FROM [AdventureWorksDW2017].[dbo].[DimProduct]'

print(fp.conexao_sql(sql)) 
