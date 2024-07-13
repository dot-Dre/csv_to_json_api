import pandas as pd
from flask import jsonify

def build_json_list(df):
    json_fields = df.columns.tolist()
    objs = []

    for index, row in df.iterrows():
        obj_map = {}
        for field in json_fields:
            obj_map[field] = row[field]
        objs.append(obj_map)

    return jsonify(objs)

def build_json_obj(df):
    json_fields = df.columns.tolist()
    obj_map = {}
    
    for field in json_fields:
        value = df.iloc[0][field]
        if isinstance(value, pd.Series):
            obj_map[field] = value.to_list()
        elif pd.api.types.is_numeric_dtype(value):
            obj_map[field] = pd.to_numeric(value).item()
        else:
            obj_map[field] = value
    
    return jsonify(obj_map)

def convert_csv_to_json(df):
    if len(df) != 1:
        build_json_list(df)
    else:
        build_json_obj(df)