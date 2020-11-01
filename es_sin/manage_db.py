from es_sin.locations import get_location_list
from es_sin.businesses import get_business_list


def get_businesses(product):
    return get_business_list(product)


def get_possible_locations(product):
    return get_location_list()
