import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Set up credentials
credentials = service_account.Credentials.from_service_account_file(
    'cobalt-vector-377412-09d0ba362f09.json',  # Update with your service account credentials file path
    scopes=['https://www.googleapis.com/auth/drive']
)

# Build the Drive service
drive_service = build('drive', 'v3', credentials=credentials)

def get_pages_from_drive(folder_id):
    """
    Lists all files in the specified folder.

    :param folder_id: ID of the folder to list files from
    """
    pages=[]
    page_token = None
    while True:
        results = drive_service.files().list(
            q=f"'{folder_id}' in parents and trashed=false",
            fields="nextPageToken, files(id, name)",
            pageToken=page_token
        ).execute()
        # print(results)
        files = results.get('files', [])
        
        if not files:
            print('No more files found in the specified folder.')
            break
        else:
            
            from_=files[0]["name"].split(" ")[0:2]
            to=files[-1]["name"].split(" ")[0:2]
            tot=len(files)
            pages.append({"from":from_,"to":to,"token_id":page_token,"tot":tot})

        page_token = results.get('nextPageToken')
        if not page_token:
            break
    return pages

if __name__ == "__main__":
    # Provide the ID of the folder you want to access
    folder_id = '10clN-KH-3B9lg4W3ProYKKoFjtpjDF61'
    # folder_id="1tMqSD61uV235vsx9c2uUIHHF0KYkqeKi"
    get_pages_from_drive(folder_id)
