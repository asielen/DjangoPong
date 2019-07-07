from __future__ import print_function
import pickle
import os.path, os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# https://docs.google.com/spreadsheets/d/12pN3tVvoZB168SVCYbhctQFtc8tV9rstNaA_DTu87to/edit#gid=0
RANKINGS_SPREADSHEET_ID = '12pN3tVvoZB168SVCYbhctQFtc8tV9rstNaA_DTu87to'
RANKINGS_RANGE_NAME = 'Games!A2:K'
HEADER_ROW = ['Team 1 Player 1 (1)', 'Team 1 Player 2 (3)', 'Team 2 Player 1 (2)', 'Team 2 Player 2 (4)', 'Team 1 Score', 'Team 2 Score', 'Datetime', 'Diff/Split', 'Winning Team', 'Window Team', 'Starting Position']

CREDENTIALS = os.path.join(os.path.dirname(os.path.realpath(__file__)),'credentials.json')
TOKEN = os.path.join(os.path.dirname(os.path.realpath(__file__)),'token.pickle')

def update_rakings_sheet(game_data=None):

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(TOKEN):
        with open(TOKEN, 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in. But only if running as main
    if not creds or not creds.valid and __name__ == '__main__':
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS, SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open(TOKEN, 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()

    # How the input data should be interpreted.
    value_input_option = 'USER_ENTERED'  # Interpret the data (instead of all strings)

    # How the input data should be inserted.
    insert_data_option = 'INSERT_ROWS'  # Add rows as needed

    if game_data:
        value_range_body = {
            "majorDimension": "ROWS",
            "values": [game_data]
        }

        request = service.spreadsheets().values().append(spreadsheetId=RANKINGS_SPREADSHEET_ID, range=RANKINGS_RANGE_NAME,
                                                     valueInputOption=value_input_option,
                                                     insertDataOption=insert_data_option, body=value_range_body)
        response = request.execute()
        # print(response)



if __name__ == '__main__':
   update_rakings_sheet()