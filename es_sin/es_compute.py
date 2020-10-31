from es_sin.features import get_valuable_features
from es_sin.manage_db import get_possible_locations
from es_sin.best_location import get_best_location


def get_product(location):
    pass


def get_location(product):
    valuable_features = get_valuable_features(product)
    possible_locations = get_possible_locations(product)
    best_location = get_best_location(possible_locations, valuable_features)
    return best_location, valuable_features[0:2]
