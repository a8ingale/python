#Run commands on EC2 instances using Lambda and Systems Manager (SendCommand)
import boto3
import botocore
import time


def handler(event=None, context=None):
    client = boto3.client('ssm')

    instance_id = 'i-07362a00952fca213' # hard-code for example
    response = client.send_command(
        InstanceIds=[instance_id],
        DocumentName='AWS-RunShellScript',
        Parameters={
            'commands': [
                # Simple test if a file exists
                'if [ -e /etc/hosts ]; then echo -n True; else echo -n False; fi'
            ]
        }
    )
    command_id = response['Command']['CommandId']
    tries = 0
    output = 'False'
    while tries < 10:
        tries = tries + 1
        try:
            time.sleep(0.5)  # some delay always required...
            result = client.get_command_invocation(
                CommandId=command_id,
                InstanceId=instance_id,
            )
            if result['Status'] == 'InProgress':
                continue
            output = result['StandardOutputContent']
            break
        except client.exceptions.InvocationDoesNotExist:
            continue

    return output == 'True'
