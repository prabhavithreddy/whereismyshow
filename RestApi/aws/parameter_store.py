import boto3
ssm = boto3.client('ssm')

def get_parameter(name:str):
    return ssm.get_parameter(Name=name)
