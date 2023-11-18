import data
import configuration
import requests


def post_new_order(body):
    return requests.post(configuration.URL_SERVICES+configuration.CREATE_ORDER,
                         json = body)
