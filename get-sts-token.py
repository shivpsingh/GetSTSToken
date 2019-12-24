#!/usr/bin/env python3

# Imports
import sys

from sts_token_mod import defaults as df
from sts_token_mod import sts_token as sts

def main(token_code, reset):
    """
        Description: 
        params: 
        return: 
    """

    sts_token = sts.STS_Connect()

    # Check - If user wants to reset the token
    if not reset:
        if sts_token.is_token_still_valid():
            print(f'STS Token is still valid - Reusing')
            df.success_message()
            return
        if token_code == None:
            print(f'STS Token has been expired - Provide new token')
            return -1

    if sts.STS_Connect().valid_token(token_code):

        AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_SESSION_TOKEN = sts_token.sts_connect(token_code)
        if AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY and AWS_SESSION_TOKEN:
            df.write_to_files(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_SESSION_TOKEN)
            df.success_message()
        else:
            print(f'ERROR: Can\'t Export Credentials: Please check!!!')
            return -1

    else:
        print(f'ERROR: Please enter valid token.')
        return -1


if __name__ == "__main__":
    """
        Description: Calling Main method for token generation
        params: 
        return: 
    """
    try:
        # gets token from user
        token_code = str(sys.argv[1])
    except IndexError as err:
        # If not provided sets to None
        token_code = None

    try:
        # gets token from user
        reset = True if str(sys.argv[2]) == 'reset' else False
    except IndexError as err:
        # If not provided sets to None
        reset = False
    
    # Calling Main method with the token code
    main(token_code, reset)
