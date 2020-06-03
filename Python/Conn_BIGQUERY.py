from pandas.io import gbq
from google.oauth2 import service_account

#Informar o arquivo json das credenciais
credentials = service_account.Credentials.from_service_account_file('C:\\Users\\bruno\\OneDrive\\BigQUery\\BigQuery-d49b6d4c827c.json')

#Cria uma consulta com as credenciais do BQ e o Project ID
df = gbq.read_gbq('select * from bigquery-194320.BP_GA_CD.Vendas_DT_Prod_Camp_Regiao LIMIT 10', project_id='bigquery-194320', credentials=credentials)

#Retorna a consulta em um DF
print(df.head())
