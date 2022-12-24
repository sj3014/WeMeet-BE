import boto3
from config import Config
import json

def send_email_sns(to, subject, body):
    topic_arn = "arn:aws:sns:us-east-1:467428421438:NewGroupMemberDetected"
    sns = boto3.client('sns',
        region_name='us-east-1',
        aws_access_key_id=Config.AWS_SNS_ACCESSKEY,
        aws_secret_access_key= Config.AWS_SNS_SECRETKEY
    )
    message = {
        "to": to,
        "subject": subject,
        "body": body
    }
    response = sns.publish(
        TopicArn=topic_arn,
        Message=json.dumps(message)
    )
    return response