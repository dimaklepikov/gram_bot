import requests
import os
import utils

HUBBLE_URL_TEMPLATE = 'http://hubblesite.org/api/v3/'

    
def fetch_hubble_image(*ids):
    for id in ids:
        url = '{}image/{}'.format(HUBBLE_URL_TEMPLATE, id)
        response = requests.get(url)
        response.raise_for_status()
        resp_body = response.json()
        images = resp_body['image_files']
        full_url = "https:{}".format(images[-1]['file_url'])
        utils.get_file(full_url, "hubble{}{}".format(id, os.path.splitext(full_url)[-1]))

fetch_hubble_image(1)
def get_hubble_collection_pics(collection):
    response = requests.get('{}images/{}'.format(HUBBLE_URL_TEMPLATE, collection))
    response.raise_for_status()
    resp_body = response.json()
    for ids in resp_body:
        fetch_hubble_image(ids["id"])

