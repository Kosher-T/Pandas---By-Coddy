import pandas as pd


def csv_convertor(filename):
    # Write code here
    try:
        df = pd.read_csv(filename)
        if df.empty:
            print("Empty file")
        else:
            print(df)
    except Exception as e:
        print("Empty file")
