import pandas as pd
import gspread
from configs.data_path_configs import SHEET_ID
from oauth2client.service_account import ServiceAccountCredentials
from df2gspread import df2gspread as d2g
import pygsheets


def upload_df(data):

    # gc = gspread.service_account(filename='getting_data/prj-22-381818-634677e6b4bc.json')
    # sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1ZuVcGNJi1CYM0KBvdQIeDHpThvfZ4r3N/edit?usp=sharing&ouid=107378308729204181621&rtpof=true&sd=true')
    # worksheet = sh.worksheet('Correlation')

    # worksheet.update([data.columns.values.tolist()] + data.values.tolist())

    scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'credentials.json', scope)
    gc = gspread.authorize(credentials)
    spreadsheet_key = SHEET_ID
    wks_name = 'Correlation'
    d2g.upload(data, spreadsheet_key, wks_name, credentials=credentials, row_names=True)


def write_to_gsheet(service_file_path, spreadsheet_id, sheet_name, data_df):
    """
    this function takes data_df and writes it under spreadsheet_id
    and sheet_name using your credentials under service_file_path
    """
    gc = pygsheets.authorize(service_file=service_file_path)
    sh = gc.open_by_key(spreadsheet_id)
    try:
        sh.add_worksheet(sheet_name)
    except:
        pass
    wks_write = sh.worksheet_by_title(sheet_name)
    wks_write.clear('A1',None,'*')
    wks_write.set_dataframe(data_df, (1,1), encoding='utf-8', fit=True)
    wks_write.frozen_rows = 1