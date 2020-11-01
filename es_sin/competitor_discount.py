from es_sin.businesses import get_business_list
from es_sin.locations import get_location_list


def discount(score, count):
    return score / (count + 1)


def discount_scores(product, scores):
    businesses = get_business_list(product)
    locations = get_location_list()
    location_counts = {}
    for location in locations:
        count = businesses[businesses['District'] == location].shape[0]
        location_counts[location] = count
    res_scores = []
    for location, score in scores:
        count = location_counts[location]
        res_scores.append((location, discount(score, count)))
    return res_scores
