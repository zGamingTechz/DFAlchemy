import pandas as pd
import json

def to_dataframe(data):
    if not data:
        raise Exception("Please insert a List, Tuple, Dictionary or Json to convert to Dataframe")

    if isinstance(data, pd.DataFrame):
        return data
    elif isinstance(data, dict):
        return pd.DataFrame([data]) if not all(isinstance(v, list) for v in data.values()) else pd.DataFrame(data)
    elif isinstance(data, list) or isinstance(data, tuple):
        return pd.DataFrame(data)
    elif isinstance(data, str):
        try:
            parsed = json.loads(data)
            return pd.DataFrame(parsed)
        except json.JSONDecodeError:
            raise ValueError("Provided string is not valid JSON.")
    else:
        raise TypeError("Unsupported data type for conversion to DataFrame.")
