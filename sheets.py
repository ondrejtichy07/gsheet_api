import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("template").sheet1

data = sheet.get_all_records()


def new_record(list_var):
    new_row = len(sheet.get_all_values()) + 1
    sheet.insert_row(list_var,index=new_row)

new_record(["test"])


