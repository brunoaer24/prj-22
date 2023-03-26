import pandas as pd


from configs.data_path_configs import SHEET_ID, SHEET_NAME



def read_data(
        sheet_id = SHEET_ID,
        sheet_name = SHEET_NAME
):
    sheet_id = "1ZuVcGNJi1CYM0KBvdQIeDHpThvfZ4r3N"
    sheet_name = "Data"

    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"


    df = pd.read_csv(url,decimal=',')

    return df[df['is_ready'] == 1] 