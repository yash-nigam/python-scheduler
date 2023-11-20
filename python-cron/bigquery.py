from google.cloud import bigquery

def check_last_modified_time(project_id, dataset_id, table_id):
    # Construct a BigQuery client
    client = bigquery.Client(project=project_id)

    # Construct the SQL query
    query = f"""
        SELECT TIMESTAMP_MILLIS(last_modified_time) AS last_modified
        FROM `{project_id}.{dataset_id}.__TABLES__ where table_id={table_id}`
    """

    # Run the query
    query_job = client.query(query)

    # Get the results
    results = query_job.result()

    # Extract and print the last modified time
    for row in results:
        print(f"Last Modified Time: {row['last_modified']}")

if __name__ == "__main__":
    # Replace with your Google Cloud project ID, dataset ID, and table ID
    project_id = "development-317013"
    dataset_id = "test"
    table_id = "titanic"

    check_last_modified_time(project_id, dataset_id, table_id)