import pandas as pd
data_path = 'data/'

location_df = None


def init_locations():
    global location_df
    df = pd.read_excel(data_path + 'Датасет (Департамент информационных технологий города Москвы).xlsx')
    districts = df['house_district'].unique()
    location_df = pd.DataFrame({'district': districts})
    ages = df['Возрастной класс'].unique()
    genders = df['person_gender'].unique()
    for age in ages:
        for gender in genders:
            label = gender + ':' + age
            count_list = []
            for district in districts:
                count_list.append(df[(df['house_district'] == district) &
                                     (df['Возрастной класс'] == age) &
                                     (df['person_gender'] == gender)]['sum'].sum())
            location_df[label] = count_list


init_locations()


def get_location_list():
    return location_df['district']


def get_location_features(location):
    return location_df[location_df['district'] == location]
