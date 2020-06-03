from google.cloud import bigquery
from google.oauth2 import service_account
import pandas as pd

credentials = service_account.Credentials.from_service_account_file('C:\\Users\\bruno\\OneDrive\\BigQUery\\BigQuery-d49b6d4c827c.json')

project_id = "bigquery-194320"

client = bigquery.Client(credentials=credentials,project=project_id)

#query_job = client.query("""
#select "date",
#    "campaign",
#    "Region",
#    "SKU",
#    "NOME",
#    "CATEGORIA",
#    "MARCA",
#    "RBV",
#    "qtde"
#from bigquery-194320.BP_GA_CD.Vendas_DT_Prod_Camp_Regiao 
#LIMIT 1000 """)

sql = """
select "date",
    "campaign",
    "Region",
    "SKU",
    "NOME",
    "CATEGORIA",
    "MARCA",
    "RBV",
    "qtde"
from bigquery-194320.BP_GA_CD.Vendas_DT_Prod_Camp_Regiao 
LIMIT 1000 """

query_config = bigquery.QueryJobConfig(use_legacy_sql=False)

#df = query_job.result()

df = client.query(sql, job_config=query_config).to_dataframe()

print(df)

