from os import path, environ

# All Fields are mandatory

AWS_CRED_ARN_FILE_NAME = path.join(environ['USERPROFILE'], '.aws', 'aws.cred.arn')
AWS_CRED_RESPONSE_FILE_NAME = path.join(environ['USERPROFILE'], '.aws', 'aws.cred.expiration')
AWS_CRED_BASH_FILE_NAME = path.join(environ['USERPROFILE'], '.aws', 'aws.bash.env')
AWS_CRED_WIN_FILE_NAME = path.join(environ['USERPROFILE'], 'sts', 'set-token.bat')

# For Hardcoding - Uncomment below lines

# AWS_CRED_ARN_FILE_NAME = ""
# AWS_CRED_RESPONSE_FILE_NAME = ""
# AWS_CRED_BASH_FILE_NAME = ""
# AWS_CRED_WIN_FILE_NAME = ""