import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

import gspread
from google.oauth2.service_account import Credentials
cred_file='cobalt-vector-377412-09d0ba362f09.json'



def get_gsheet_data(sheet_id):
    # credentials = Credentials.from_service_account_file(cred_file, scopes=['https://www.googleapis.com/auth/spreadsheets'])

    gc = gspread.authorize(credentials)
    worksheet = gc.open_by_key(sheet_id).sheet1
    all_values = worksheet.get_all_values()
    print(f"sheet id  is , {sheet_id}")
    for row in all_values:
        print(row)

credentials = service_account.Credentials.from_service_account_file(
    cred_file,  
    scopes=['https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/spreadsheets']
)


drive_service = build('drive', 'v3', credentials=credentials)

def list_files_in_folder(folder_id):
    """
    Lists all files in the specified folder.

    :param folder_id: ID of the folder to list files from
    """
    
    results = drive_service.files().list(
        q=f"'{folder_id}' in parents and trashed=false",
        fields="files(id, name)"
    ).execute()
    files = results.get('files', [])
    if not files:
        print('No files found in the specified folder.')
    elif len(files)==1:
        sheet_id=files[0]['id']
        print(files[0])
        print(files[0]["name"])
        date=files[0]["name"].split(" ")[0]
        time=files[0]["name"].split(" ")[1]
        gmeet_title=files[0]["name"].split(" ")[2]
        sheet_link=files[0]["id"]
      
        # get_gsheet_data(sheet_id)

    else:
        for file in files:
            list_files_in_folder(file['id'])
    
            
            

if __name__ == "__main__":
    # Provide the ID of the folder you want to access
    folder_id = '10clN-KH-3B9lg4W3ProYKKoFjtpjDF61'

    print(list_files_in_folder(folder_id))
