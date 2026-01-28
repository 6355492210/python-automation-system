from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import pickle
import os

def Create_Service(client_secret_file, api_name, api_version, scopes):
    creds = None
    token_file = f"token_{api_name}_{api_version}.pickle"

    if os.path.exists(token_file): #logi che k ny check
        with open(token_file, "rb") as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            client_secret_file, scopes
        )
        creds = flow.run_local_server(port=0)

        with open(token_file, "wb") as token:
            pickle.dump(creds, token)

    service = build(api_name, api_version, credentials=creds)
    return service
