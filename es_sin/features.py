from es_sin.manage_db import get_businesses
from es_sin.score_business import get_score
from es_sin.locations import get_location_features
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import pandas as pd


def get_top_businesses(business_scores):
    return business_scores


def filter_features(columns, location_features, business_scores):
    sc = StandardScaler()
    frame = pd.DataFrame(location_features, columns=columns)
    X = sc.fit_transform(frame)
    X = pd.DataFrame(X, columns=columns)
    y = pd.DataFrame(business_scores, columns=['business_score'])
    model = LinearRegression().fit(X, y)
    return model.coef_

    return location_features


def get_valuable_features(product_frame):
    businesses = get_businesses(product_frame)
    business_scores = zip(businesses.District.values, get_score(businesses))
    # top_businesses = get_top_businesses(business_scores)
    # locations = [business.location for business in top_businesses]
    columns, location_features = [get_location_features(location) for location, _ in business_scores]
    target_scores = [score for _, score in business_scores]
    return filter_features(columns, location_features, target_scores)