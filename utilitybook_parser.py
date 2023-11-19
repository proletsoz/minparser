import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Подключение к Google Sheets API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'credentials.json', scope)
gc = gspread.authorize(credentials)

spreadsheet_id = '1tdFxwZ6H4i7nSMxZfrAW-ViPGd3CAa0vu62gJcllTP0'
worksheet = gc.open_by_key(spreadsheet_id).sheet1

# Получение значений
values = worksheet.get_all_values()

# Вывод значений
for row in values:
    print(row)
