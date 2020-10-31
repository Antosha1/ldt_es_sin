from es_sin.manage_db import get_businesses
from es_sin.score_business import get_score
from es_sin.locations import get_location_features, get_columns
from sklearn.linear_model import LinearRegression

import pandas as pd


def get_top_businesses(business_scores):
    return business_scores


def filter_features(columns, location_features, business_scores, sc):
    frame = pd.DataFrame(location_features, columns=columns[1:])
    X = sc.fit_transform(frame)
    X = pd.DataFrame(X, columns=columns[1:])
    y = pd.DataFrame(business_scores, columns=['business_score'])
    model = LinearRegression().fit(X, y)
    return model.coef_


def get_valuable_features(product_frame, sc):
    businesses = get_businesses(product_frame)
    target_scores = get_score(businesses)
    business_scores = zip(businesses.District.values, target_scores)
    # top_businesses = get_top_businesses(business_scores)
    # locations = [business.location for business in top_businesses]
    location_features = [get_location_features(location) for location, _ in business_scores]
    columns = get_columns()
    return zip(columns, filter_features(columns, location_features, target_scores, sc))