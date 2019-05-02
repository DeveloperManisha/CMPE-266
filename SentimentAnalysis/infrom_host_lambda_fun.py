import boto3
import time


ses = boto3.client('ses')

email_from = 'manisha.shivshette@sjsu.edu'
email_to = 'shivshette.manisha@gmail.com'
email_cc = 'manisha.shivshette@sjsu.edu'
emaiL_subject = 'Alert:Negative Review for your property '
email_body = 'review '
def send():
    response = ses.send_email(
        Source = email_from,
        Destination={
            'ToAddresses': [
                email_to,
            ],
            'CcAddresses': [
                email_cc,
            ]
        },
        Message={
            'Subject': {
                'Data': emaiL_subject
            },
            'Body': {
                'Text': {
                    'Data': email_body
                }
            }
        })



def executeSQL():
     # created query
    query = "SELECT * FROM default.ReviewSentimentAnalysis where sentiment='NEGATIVE'"
    # athena client
    client = boto3.client('athena')

    # Execution
    response = client.start_query_execution(
        QueryString=query,
        QueryExecutionContext={
            'Database': 'default'
        },
        ResultConfiguration={
            'OutputLocation': 's3://review-sentiment-s3-t3gxkbupxju9',
        }
    )

    # get query execution id
    query_execution_id = response['QueryExecutionId']
    print(query_execution_id)

    # get execution status
    for i in range(1, 11):

        # get query execution
        query_status = client.get_query_execution(QueryExecutionId=query_execution_id)
        query_execution_status = query_status['QueryExecution']['Status']['State']

        if query_execution_status == 'SUCCEEDED':
            print("STATUS:" + query_execution_status)
            break

        if query_execution_status == 'FAILED':
            raise Exception("STATUS:" + query_execution_status)

        else:
            print("STATUS:" + query_execution_status)
            time.sleep(i)
    else:
        client.stop_query_execution(QueryExecutionId=query_execution_id)
        raise Exception('TIME OVER')

    # get query results
    result = client.get_query_results(QueryExecutionId=query_execution_id)
    return result


def lambda_handler(event, context):
   
    result = executeSQL()
    if len(result['ResultSet']['Rows']) > 0:
         send()

