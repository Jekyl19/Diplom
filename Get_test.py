#Глеб Таличкин, 10-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request
import data
import requests
import configuration

def test_can_get_order_by_track():
    response = sender_stand_request.post_new_order(data.order_body)
    order_track = response.json()['track']
    assert requests.get(configuration.URL_SERVICES+configuration.GET_ORDER_BY_TRACK +
                        str(order_track)).status_code == 200