import os
import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

CLIENT_SECRETS_FILE = "client_secret.json"

SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'


def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_console()
    # credentials = "4/aQD1OO80qe0-n0z9H6I95wV1IGOiqS0V-jpPUxEYEoLPlwMVheFvXtw"
    return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)


def print_response(response):
    print(response)


# remove keyword arguments that are not set
def remove_empty_kwargs(**kwargs):
    good_kwargs = {}
    if kwargs is not None:
        for key, value in kwargs.items():  # iteritems should be .items?
            if value:
                good_kwargs[key] = value
    return good_kwargs