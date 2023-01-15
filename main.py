from google.cloud import bigquery
import sqlparse
import sys

try:
    client = bigquery.Client()
    print('Connection to Google BigQuery Success')
except:
    print('Connection to Google BigQuery Failed')

client.create_dataset(sys.argv[1], exists_ok=True)
dataset = client.dataset(sys.argv[1])
table_ref = bigquery.TableReference(dataset, sys.argv[2])
table = bigquery.Table(table_ref, schema=None)

file = open('query.sql', 'r').read()
sql = sqlparse.format(file)
job_config = bigquery.QueryJobConfig(allow_large_results=True, destination=table, write_disposition='WRITE_TRUNCATE')
query_job = client.query(sql, job_config=job_config)
results = query_job.result()

print('Query Results Loaded to the Table')