from es_sin.manage_db import get_businesses
from es_sin.score_business import get_score


def get_top_businesses(business_scores):
    return business_scores


def filter_features(location_features):
    return location_features


def get_valuable_features(product):
    businesses = get_businesses(product)
    business_scores = [(business, get_score(business))
                       for business in businesses]
    top_businesses = get_top_businesses(business_scores)
    locations = [business.location for business in top_businesses]
    location_features = [location.features for location in locations]
    return filter_features(location_features)
