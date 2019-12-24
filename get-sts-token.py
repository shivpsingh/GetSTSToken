#!/usr/bin/env python3
"""
    Author		: Shiv Pratap Singh
    Description	: Script for STS Token Credentials
"""

# Imports
import sys

# Custom Imports
from sts_token_mod import sts_token as sts

def mapper(splitter, arg_list):
    data = dict()
    for arg in arg_list:
        try:
            key = str(arg).split(splitter)[0]
            value = str(arg).split(splitter)[1]
            data[key] = value
        except Exception:
            pass
    return data

def main(token_code, reset, profile):
    """
        Description	: Calling STS_Connect Class to check for credentails
        params		: 
            - token_code  : 6 Digit MFA Code
            - reset       : flag for generating a new token
        
        return		: -1 for error and 0 for success
    """

    # Check - If user wants to reset the token
    if not reset:
        if sts.STS_Connect.is_token_still_valid():
            print(f'STS Token is still valid - Reusing')
            sts.STS_Connect.sts_success_msg()
            return
        if token_code == None:
            print(f'STS Token has been expired - Provide new token')
            return -1

    if sts.STS_Connect.valid_token(token_code):
        sts_token = sts.STS_Connect(profile)

        if sts_token.create_sts_scripts(token_code):
            sts.STS_Connect.sts_success_msg()
        else:
            print(f'ERROR: Can\'t Export Credentials: Please check!!!')
            return -1
    else:
        print(f'ERROR: Please enter valid token.')
        return -1


if __name__ == "__main__":

    results = mapper("=", sys.argv)
    arg_keys = results.keys()

    token_code = results['-t'] if '-t' in arg_keys else None
    reset = (True if results['-r'] == 'reset' else False) if '-r' in arg_keys else False

    if '-p' in arg_keys:
        profile = results['-p']
    else:
        print('INFO: Profile name is not provided - Using default')
        profile = sts.STS_Connect.sts_default_profile()
    
    # Calling Main method with the token code
    main(token_code, reset, profile)
