from os import path, environ
import json

# Defaults

AWS_CRED_ARN_FILE_NAME = path.join(environ['USERPROFILE'], '.aws', 'aws.cred.arn')
AWS_CRED_RESPONSE_FILE_NAME = path.join(environ['USERPROFILE'], '.aws', 'aws.cred.expiration')
AWS_CRED_BASH_FILE_NAME = path.join(environ['USERPROFILE'], '.aws', 'aws.bash.env')
AWS_CRED_WIN_FILE_NAME = path.join(environ['USERPROFILE'], 'sts', 'set-token.bat')
# AWS_CRED_WIN_FILE_NAME = path.join(environ['USERPROFILE'], '.aws', 'aws.win.bat')

PROFILE = 'default'

try:
    with open(AWS_CRED_ARN_FILE_NAME, 'r') as fh:
        ARN_DICT = json.load(fh)
except FileNotFoundError as ferr:
    print(f'ERROR: Credentials File not found.')
    print(f'Please create File: {AWS_CRED_ARN_FILE_NAME}')

def get_arn(profile):
    return ARN_DICT[profile]

def success_message():
    print('For Setting credentials for current shell : Run below commands')
    bash_file_name = str(AWS_CRED_BASH_FILE_NAME).replace('\\', '\\\\')
    print(f'For Bash RUN: . {bash_file_name}')
    print(f'For Windows RUN: {AWS_CRED_WIN_FILE_NAME}')


def write_to_files(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_SESSION_TOKEN):
    try:
        # For Bash terminal
        with open(AWS_CRED_BASH_FILE_NAME, 'w') as fh:
            fh.write(f'export AWS_ACCESS_KEY_ID="{AWS_ACCESS_KEY_ID}"\n')
            fh.write(f'export AWS_SECRET_ACCESS_KEY="{AWS_SECRET_ACCESS_KEY}"\n')
            fh.write(f'export AWS_SESSION_TOKEN="{AWS_SESSION_TOKEN}"')
        # For CMD
        with open(AWS_CRED_WIN_FILE_NAME, 'w') as fh:
            fh.write(f'@echo off\n')
            fh.write(f'set AWS_ACCESS_KEY_ID={AWS_ACCESS_KEY_ID}\n')
            fh.write(f'set AWS_SECRET_ACCESS_KEY={AWS_SECRET_ACCESS_KEY}\n')
            fh.write(f'set AWS_SESSION_TOKEN={AWS_SESSION_TOKEN}\n')
            fh.write(f'echo AWS STS Credentials has been set.')
    except Exception:
        return False
        
    return True
