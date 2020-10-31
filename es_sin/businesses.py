import pandas as pd
data_path = 'data/'

business_df = None


def init_businesses():
    global business_df
    business_df = pd.read_csv(data_path + 'dotaframe.csv', sep='\t')


init_businesses()


def get_business_list(product):
    return business_df[business_df['Product'] == product]
