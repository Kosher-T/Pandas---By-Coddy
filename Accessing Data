import pandas as pd
def specific_returner(file_name, value):
    # Write code here
    df = pd.read_csv(file_name)
    try:
        value = int(value)
        row = df.iloc[value]
        return row
    except Exception:
        column = df[value]
        return column
