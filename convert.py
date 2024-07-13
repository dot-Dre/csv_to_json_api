import pandas as pd
from flask import jsonify

def build_json_list(df):
    """
    Build a JSON list from a pandas DataFrame.

    Args:
        df (pd.DataFrame): Pandas DataFrame containing the data to convert.

    Returns:
        jsonify: JSON response containing a list of objects, each representing a row in the DataFrame.
    """
    json_fields = df.columns.tolist()
    objs = []

    for index, row in df.iterrows():
        obj_map = {}
        for field in json_fields:
            obj_map[field] = row[field]
        objs.append(obj_map)

    return jsonify(objs)

def build_json_obj(df):
    """
    Build a JSON object from the first row of a pandas DataFrame.

    Args:
        df (pd.DataFrame): Pandas DataFrame containing the data to convert.

    Returns:
        jsonify: JSON response containing an object representing the first row of the DataFrame.
    """
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
    """
    Convert a pandas DataFrame to JSON format based on its size.

    Args:
        df (pd.DataFrame): Pandas DataFrame containing the data to convert.

    Returns:
        jsonify: JSON response containing either a list of objects (if DataFrame size > 1)
                 or an object (if DataFrame size == 1).
    """
    if len(df) != 1:
        return build_json_list(df)
    else:
        return build_json_obj(df)
