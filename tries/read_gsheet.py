import gspread
from google.oauth2.service_account import Credentials

# Replace 'YOUR_CREDENTIALS_FILE.json' with the path to your credentials JSON file
credentials = Credentials.from_service_account_file(r'D:\gokul_repos\access-gmeet-logs\tries\cobalt-vector-377412-09d0ba362f09.json', scopes=['https://www.googleapis.com/auth/spreadsheets'])

# Replace '149MKx7OYkUhPntGVmpZsIGOJhLQo0TrV7r4W_5muRxw' with your actual Google Sheet ID
sheet_id = '149MKx7OYkUhPntGVmpZsIGOJhLQo0TrV7r4W_5muRxw'

# Authorize the API
gc = gspread.authorize(credentials)

# Open the Google Sheet
worksheet = gc.open_by_key(sheet_id).sheet1

# Get all values from the sheet
all_values = worksheet.get_all_values()

# Print the content
for row in all_values:
    print(row)
