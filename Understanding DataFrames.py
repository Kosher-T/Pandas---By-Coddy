import pandas as pd


def information(action):
    # Write code here
    df = pd.read_csv("brands.csv")

    if action == 'head':
        print(df.head())
    if action == 'tail':
        print(df.tail())
    if action == 'describe':
        print(df.describe())
    if action == 'info':
        print(df.info())
    if action == 'shape':
        print(df.shape)
