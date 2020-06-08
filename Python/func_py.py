#Conexão SQL Server
import pyodbc
import pandas as pd

def conexao_sql(select):
    #Informar o servidor
    server = 'DESKTOP-QRGC4CU\SQLEXPRESS'
    #Informar o DataBase
    database = 'AdventureWorksDW2017'
    #Instreing de Conexão
    string_conexao = 'Driver={SQL Server Native Client 11.0};Server='+server+';Database='+database+';Trusted_connection=yes;'
    #Abre a conexão
    conexao = pyodbc.connect(string_conexao)
    # Executa a Consulta  
    sql_query = pd.read_sql(select,conexao)
    # Armazena a Consulta no DF (Precisa nomear os campos e colocar quantos campos tem a conmsulta - (index))
    df = pd.DataFrame(sql_query,columns = ['ProductKey','ProductAlternateKey'])
    #Fecha a conexao
    conexao.close()
    #Retorna a consulta
    return df

#Executar 
#import func_py as fp
#sql = 'SELECT * FROM ......'
#fp.conexao_sql(sql) 

#------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------
#Conexão BigQuery
from pandas.io import gbq
from google.oauth2 import service_account

def conexao_bq(select):
    #Informar o arquivo json das credenciais EXTRAIDAS DO GCP
    credentials = service_account.Credentials.from_service_account_file('C:\\Users\\bruno\\OneDrive\\BigQUery\\BigQuery-d49b6d4c827c.json')
    #Cria uma consulta com as credenciais do BQ e o Project ID
    df = gbq.read_gbq(select, project_id='bigquery-194320', credentials=credentials)
    #Retorna a consulta
    return df

#Executar 
#import func_py as fp
#sql = 'SELECT * FROM ......'
#fp.conexao_bq(sql) 
