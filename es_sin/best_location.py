from es_sin.locations import get_location_features


def get_best_location(possible_locations, valuable_features, sc):
    coefs = valuable_features
    res_list = []
    for location in possible_locations:
        features = get_location_features(location)
        norm_features = sc.transform([features])
        location_score = coefs.dot(norm_features.T)
        res_list.append((location, location_score))
    res_list = sorted(res_list, key=lambda x: x[1], reverse=True)
    return res_list[0][0]