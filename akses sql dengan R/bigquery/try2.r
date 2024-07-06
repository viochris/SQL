library(bigrquery)

# Set path to JSON service account key
Sys.setenv(GOOGLE_APPLICATION_CREDENTIALS="D:\\Program Files\\fifth-citadel-428301-k3-2afc36d9b323.json")

# Establish BigQuery connection
project <- "fifth-citadel-428301-k3"


# Query to execute
query <- "
SELECT *
FROM `bigquery-public-data.google_trends.top_terms`
LIMIT 10
"

# Execute query
query_result <- bq_project_query(project, query)

# Download query result to DataFrame
result_df <- bq_table_download(query_result)

# Show DataFrame
print(result_df)
