# GetSTSToken

Requirements:

```
    1. Python3.6 or latest
    2. aws credentials should be configured - using aws configure
    3. python boto3 package - pip install boto3
```

Create a aws.cred.arn file in HOME Directory
For windows user %USERPROFILE%\.aws Directory
For Linux user ~/.aws

copy below code content to cred file replacing arn:

```
{
    "default": "<mfa_arn>"
}
```

Create a sts directory in your home

For Windows:
```
    mkdir %USERPROFILE%\sts
```
For Linux 
```
    mkdir ~/sts
```
Now clone the code into this directory using below command

```
    git clone <clone_url> .
```

Set sts directory into Environment Variables

Now to create sts token scripts run:

For default Profile

```
    get-sts-token.py -t=<token_code>
```

For Custom Profile

```
    get-sts-token.py -t=<token_code> -p=<profile_name>
```

For Reset Existing token

```
    get-sts-token.py -t=<token_code> -r=reset
```

For Reset Existing token For Custom Profile

```
    get-sts-token.py -t=<token_code> -r=reset -p=<profile_name>
```

To Set credentials in CMD / Powershell Run:
```
    set-token.bat
```

#### If want to use custom locations for the files, please update sts_token_mod/locations.py

--- 

Shiv Pratap Singh
