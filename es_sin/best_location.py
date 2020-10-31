from es_sin.locations import get_location_features, get_columns
import pandas as pd
import numpy as np


def get_best_location(possible_locations, valuable_features, sc):
    columns = get_columns()
    coefs = pd.DataFrame([np.zeros(len(columns) - 1)], columns=columns[1:])
    for feature, coef in valuable_features:
        coefs[feature][0] = coef
    coefs = np.array(coefs).flatten()
    res_list = []
    for location in possible_locations:
        features = get_location_features(location)
        norm_features = sc.transform([features])
        location_score = coefs.dot(norm_features.T)
        res_list.append((location, location_score))
    res_list = sorted(res_list, key=lambda x: x[1], reverse=True)
    return res_list[0][0]
