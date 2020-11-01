from es_sin.features import get_valuable_features
from es_sin.manage_db import get_possible_locations
from es_sin.best_location import get_best_location
from sklearn.preprocessing import StandardScaler


sc = StandardScaler()


def get_product(location):
    pass


def get_location(product):
    valuable_features = get_valuable_features(product, sc)
    if not valuable_features:
        return '', []
    possible_locations = get_possible_locations(product)
    best_location = get_best_location(product, possible_locations, valuable_features, sc)
    return best_location, [feature for feature, _ in valuable_features]
