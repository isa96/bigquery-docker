### Upload query results to Google BigQuery table with Google Cloud SDK on Docker

##### Clone this repository and enter the directory
> git clone [https://github.com/yevadrian/bigquery-docker](https://github.com/isa96/bigquery-docker.git) && cd bigquery-docker

##### Modify "key.json" according to your Google service account credentials
> nano key.json

##### Modify "query.sql" according to your query needs
> nano query.sql

##### Create Google Cloud SDK container with Docker Compose
> sudo docker compose up -d

##### Install required Python packages
> sudo docker exec -it gcloud sh -c "pip install google-cloud-bigquery && pip install sqlparse"

##### Run the Python script to upload query results to your Google BigQuery
> sudo docker exec -it gcloud sh -c "python3 main.py [DATASET] [TABLE]"

##### Example command
> sudo docker exec -it gcloud sh -c "python3 main.py aaa results"
