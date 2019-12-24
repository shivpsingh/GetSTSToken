import boto3
from datetime import datetime, timedelta
from dateutil import tz
from dateutil.tz import tzutc
import pickle as pk
import re

from . import defaults as df


class STS_Connect:
    
    def __init__(self, profile=df.PROFILE):
        self.__profile = profile
        self.__session = boto3.Session(profile_name=self.__profile) # type: botostubs.session

    def sts_connect(self, token_code):

        self.__sts = self.__session.client('sts') # type: botostubs.sts

        try:
            response = self.__sts.get_session_token(
                SerialNumber=df.get_arn(self.__profile),
                TokenCode=token_code
            )
        except Exception as err:
            print(f'ERROR: {str(err)}')
            return -1

        expiration_time = response['Credentials'].get('Expiration', None)

        with open(df.AWS_CRED_RESPONSE_FILE_NAME, 'wb') as fh:
            pk.dump(expiration_time, fh)

        AWS_ACCESS_KEY_ID = response['Credentials'].get('AccessKeyId', None)
        AWS_SECRET_ACCESS_KEY = response['Credentials'].get('SecretAccessKey', None)
        AWS_SESSION_TOKEN = response['Credentials'].get('SessionToken', None)

        return AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_SESSION_TOKEN

    def is_token_still_valid(self):
        current_time = datetime.now(tz.UTC)
        last_exp_time = current_time
        with open(df.AWS_CRED_RESPONSE_FILE_NAME, 'rb') as fh:
            try:
                last_exp_time = pk.load(fh)
            except EOFError as err:
                last_exp_time = current_time
        if last_exp_time > current_time:
            return True
        return False

    @classmethod
    def valid_token(cls, token_code):
        VALID_PATTERN = "^[0-9]{6}$"
        pattern = re.compile(VALID_PATTERN)
        return True if pattern.match(token_code) else False