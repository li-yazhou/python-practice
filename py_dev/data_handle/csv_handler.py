import numpy as np
import pandas as pd


read_file = "../data/data.csv"
write_file = "../data/data_bak.csv"
# headers = ['id', 'zone', 'cpu', 'memory', 'proposer']


def load_data(file):
    # df = pd.read_csv(file, header=None, sep=' ')
    return pd.read_csv(file, header=0, sep=',')


def write_data(df):
    df.to_csv(write_file, index=None)


df_0 = load_data(read_file)
df_1 = load_data('../data/data_1.csv')
df = pd.merge(df_0, df_1, how='outer', on=['id'])

print(df)
write_data(df)


