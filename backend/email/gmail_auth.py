from google_auth_oauthlib.flow import Flow
from googleapiclient import build
from google.oauth2.credentials import Credentials

SCOPES = ["https://www.googleapis.com/auth.gmail.modify"]

def get_gmail_service(creds):
    return build("gmail", "v1" , credentials=creds)

