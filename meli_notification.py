import requests


def send_meli_shipment_notification(ids: list):
    url = 'https://ppointapi.clicoh.com/api/v1/mercadolibre/notifications/'

    heathers = {"Content-Type": "application/json"}
    sesion = requests.session()
    for number in ids:
        body = {"_id": "59ab2448-9e4b-4acc-9df2-4c0c10f69616",
                "topic": "shipments",
                "resource": f"/shipments/{number}",
                "user_id": "651964590",
                "application_id": "2837633607706386",
                "sent": "2022-06-14T15:55:11.802Z",
                "attempts": "1",
                "received": "2022-06-14T15:55:11.655Z"
                }
        response=sesion.post(url=url,headers=heathers, json=body)


if __name__ == '__main__':
    #fill the ids array with meli shipings ids
    #format ids = ["id1", "id2", ....]
    ids =  []

    #IMPORTANT: this script works only for the client adabra to change de store change de user_id on the body
    send_meli_shipment_notification(ids)
