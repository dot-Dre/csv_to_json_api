import pandas as pd

def build_json_list(df):
    pass

def build_json_obj(df):
    pass

def convert_csv_to_json(df):
    if len(df) != 1:
        build_json_list(df)
    else:
        build_json_obj(df)