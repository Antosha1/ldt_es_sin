import pandas as pd
data_path = 'data/'

busines_df = None


def init_businesses():
    global busines_df
    busines_df = pd.read_csv(data_path + 'dotaframe.csv', sep='\t')


init_businesses()
print(busines_df)


def get_business_list(product):
    return busines_df[busines_df['Product'] == product]
