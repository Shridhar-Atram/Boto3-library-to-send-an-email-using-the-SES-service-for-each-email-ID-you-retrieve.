import boto3
import json

def lambda_handler(event, context):
    # Retrieve email IDs from the S3 file
    s3_bucket = event['Records'][0]['s3']['bucket']['name']
    s3_key = event['Records'][0]['s3']['object']['key']  # Provide the path to your file in the S3 bucket

    s3_client = boto3.client('s3')
    s3_object = s3_client.get_object(Bucket=s3_bucket, Key=s3_key)
    email_ids = s3_object['Body'].read().decode('utf-8').split('\n')

    # Send email for each email ID
    ses_client = boto3.client('ses')

    for email_id in email_ids:
        email_id = email_id.strip()  # Remove leading/trailing whitespace
        
        # Perform email sending operations using SES client
        response = ses_client.send_email(
            Source='<source email-id>',
            Destination={'ToAddresses': [email_id]},
            Message={
                'Subject': {'Data': 'Your Subject'},
                'Body': {'Text': {'Data': 'Your Email Body'}}
            }
        )
        
        print(f"Email sent to {email_id}. Message ID: {response['MessageId']}")
