from es_sin.manage_db import get_businesses
from es_sin.score_business import get_score
from es_sin.locations import get_location_features


def get_top_businesses(business_scores):
    return business_scores


def filter_features(location_features):
    return location_features


def get_valuable_features(product):
    businesses = get_businesses(product)
    business_scores = zip(businesses.District.values, get_score(businesses))
    #top_businesses = get_top_businesses(business_scores)
    #locations = [business.location for business in top_businesses]
    location_features = [get_location_features(location) for location, _ in business_scores]
    return filter_features(location_features)
