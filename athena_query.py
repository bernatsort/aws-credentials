import boto3
import time

# Create a session using the datahub profile
session = boto3.Session(profile_name='datahub')

# Create an Athena client
athena = session.client('athena', region_name='eu-west-1')

# Function to start a query execution
def start_query(query, database, output_location):
    response = athena.start_query_execution(
        QueryString=query,
        QueryExecutionContext={
            'Database': database
        },
        ResultConfiguration={
            'OutputLocation': output_location
        }
    )
    return response['QueryExecutionId']

# Function to get query execution status
def get_query_execution(query_execution_id):
    response = athena.get_query_execution(
        QueryExecutionId=query_execution_id
    )
    return response['QueryExecution']['Status']['State']

# Function to get query results
def get_query_results(query_execution_id):
    results = athena.get_query_results(
        QueryExecutionId=query_execution_id
    )
    return results

# Define your query, database, and output location
query = "SELECT COUNT(*) FROM dhdfmed3nuetlvdeveuwest1shared.audit;"
database = "dhdfmed3nuetlvdeveuwest1shared"
output_location = "s3://dhomacldataqee2qwdeveuwest1/queryresult/readcatalog/"

# Start the query execution
query_execution_id = start_query(query, database, output_location)
print(f"Query Execution ID: {query_execution_id}")

# Wait for the query to complete
status = get_query_execution(query_execution_id)
while status in ['RUNNING', 'QUEUED']:
    print("Waiting for query to complete...")
    time.sleep(5)
    status = get_query_execution(query_execution_id)

# Get the query results
if status == 'SUCCEEDED':
    results = get_query_results(query_execution_id)
    
    # Extract and print results in a readable format
    rows = results['ResultSet']['Rows']
    column_info = results['ResultSet']['ResultSetMetadata']['ColumnInfo']
    columns = [col['Name'] for col in column_info]
    
    print("Query Results:")
    for row in rows:
        for data in row['Data']:
            print(data['VarCharValue'], end='\t')
        print()
else:
    print(f"Query failed with status: {status}")

