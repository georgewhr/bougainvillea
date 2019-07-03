from __future__ import print_function
from __future__ import division
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from collections import OrderedDict

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = '1ZuisefQfOy-3AxXmlsqTDUXmuUwKQ3IhkmKoW2U5ia4'
RANGE_NAME = 'Sheet3!A2'

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)
    sheet_values=[]
    with open("all.txt", 'r') as f:
        data_agg = {}
        for line in f:
            time = line.rstrip()[0:13]
            if time not in data_agg:
                data_agg[time] = {}
                data_agg[time]['garden_temp'] = list()
                data_agg[time]['garden_hum'] = []
                data_agg[time]['hydrangea_temp'] = []
                data_agg[time]['hydrangea_moisture'] = []
            if "FE:0E:D3:CC:BD:F9" in line:
                temp = int(line.rstrip()[91:95],16)/10
                hum = int(line.rstrip()[95:99],16)/10
                if temp > 100 or hum > 100:
                    continue
                data_agg[time]['garden_temp'].append(temp)
                data_agg[time]['garden_hum'].append(hum)
                # data_agg[time].append([temp,hum])
            elif "b5b182c7eab14988aa99b5c1517008d9" in line:
                soil_moil = int(line.rstrip()[119:121],16)
                plant_temp = int(line.rstrip()[121:123],16)
                if soil_moil > 100 or plant_temp > 100:
                    continue
                data_agg[time]['hydrangea_moisture'].append(soil_moil)
                # print soil_moil
                data_agg[time]['hydrangea_temp'].append(plant_temp)
    for key1 in data_agg:
        for key2 in data_agg[key1]:
            average = sum(data_agg[key1][key2])/len(data_agg[key1][key2])
            data_agg[key1][key2] = average
    ordered = OrderedDict(sorted(data_agg.items(), key=lambda t: t[0]))
    # print (ordered)
    for i in ordered:
        temp = []
        temp.append(i)
        for j in ordered[i]:
            temp.append(ordered[i][j])
        sheet_values.append(temp)
    sheet_body = {
        'values': sheet_values
    }
    # exit(0)
    # print (sheet_values)
    # exit(0)
    # Call the Sheets API
    sheet = service.spreadsheets()

    result = service.spreadsheets().values().update(
    spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME,
    valueInputOption='USER_ENTERED', body=sheet_body).execute()
    
    # result = sheet.values().append(
    #     spreadsheetId=SPREADSHEET_ID,
    #     range=RANGE_NAME,
    #     valueInputOption='USER_ENTERED',
    #     body=sheet_body).execute()
    

if __name__ == '__main__':
    main()