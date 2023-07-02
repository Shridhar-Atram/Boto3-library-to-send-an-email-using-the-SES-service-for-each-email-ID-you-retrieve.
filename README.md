AWS Lambda Email Sending Automation with Boto3 and SES
This repository contains the code for automating email sending using AWS Lambda, Boto3, and SES. With this solution, you can easily send emails to a list of recipients stored in an S3 file.

Prerequisites
AWS account with appropriate permissions to create and configure Lambda functions, S3 buckets, and SES.
Python 3.x installed on your local machine.
AWS CLI installed and configured with your AWS credentials.
Setup
Clone this repository to your local machine.
Navigate to the project directory.
Deployment
Open the lambda_function.py file and replace <source email-id> with your desired email address.
Run the following commands to create an S3 bucket and upload the email ID file:
php
Copy code
aws s3api create-bucket --bucket <bucket-name> --region <region> --create-bucket-configuration LocationConstraint=<region>
aws s3 cp email_ids.txt s3://<bucket-name>/
Make sure to replace <bucket-name> with a unique name for your S3 bucket and <region> with the desired AWS region code (e.g., us-east-1).
Deploy the Lambda function by running the following command:
css
Copy code
aws lambda create-function --function-name sendEmails --runtime python3.8 --handler lambda_function.lambda_handler --zip-file fileb://lambda_function.zip --role <lambda-role-arn>
Replace <lambda-role-arn> with the ARN of the IAM role that allows Lambda to access S3 and SES.
Once the Lambda function is created, you need to set up an S3 trigger. Run the following command to configure the trigger:
ruby
Copy code
aws lambda add-permission --function-name sendEmails --statement-id s3invoke --action "lambda:InvokeFunction" --principal s3.amazonaws.com --source-arn arn:aws:s3:::<bucket-name> --source-account <your-account-id>
Replace <bucket-name> with the name of the S3 bucket you created, and <your-account-id> with your AWS account ID.
Finally, create an S3 event notification that triggers the Lambda function when a new file is created in the bucket:
arduino
Copy code
aws s3api put-bucket-notification-configuration --bucket <bucket-name> --notification-configuration file://s3_event_notification.json
Usage
Update the email_ids.txt file with the list of recipient email IDs, with each ID on a new line.
Save and upload the updated email_ids.txt file to the S3 bucket.
The Lambda function will automatically trigger upon detecting the new file and start sending emails to the recipients.
Monitoring
To monitor the execution of the Lambda function, you can check the CloudWatch Logs. The function will print the status of each email sent along with the corresponding message ID.

That's it! You have successfully set up email sending automation using AWS Lambda, Boto3, and SES. Feel free to customize the email subject and body in the lambda_function.py file as per your requirements.

For more information, please refer to the official AWS Lambda, S3, and SES documentation.

Happy automating! 🚀📧
