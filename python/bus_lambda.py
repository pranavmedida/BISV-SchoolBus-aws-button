from __future__ import print_function
import boto3
import json
sns_arn = "arn:aws:sns:us-east-1:<AWS_Account_Number>:Amma"
def pranav(event,context):
    sns_client = boto3.client('sns')
    output =  event['clickType'] 
    if  output == "SINGLE" :
       message_to_send = "I took the bus and starting"
    elif  bag == "DOUBLE":
       message_to_send = "Ignore my message"
    elif  bag == "LONG" :
       message_to_send = " I Might be a bit Late"
    rsp = sns_client.publish(
        TargetArn=sns_arn,
        Message=message_to_send)
