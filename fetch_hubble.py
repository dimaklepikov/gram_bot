import requests
import os
import urllib.request

HUBBLE_URL_TEMPLATE = 'http://hubblesite.org/api/v3/'

def file_download(url, name):
    urllib.request.urlretrieve(url, 'pictures/{}'.format(name))
    
def get_file_extetion(url):
    url_lst = url.split('.')
    return url_lst[-1]

def fetch_hubble_image(*ids):
    for id in ids:
        url = '{}image/{}'.format(HUBBLE_URL_TEMPLATE, id)
        response = requests.get(url)
        response.raise_for_status()
        resp_body = response.json()
        images = resp_body['image_files']
        full_url = "https:{}".format(images[-1]['file_url'])
        file_download(full_url, "hubble{}.{}".format(id, get_file_extetion(full_url)))


def get_hubble_collection_pics(collection):
    response = requests.get('{}images/{}'.format(HUBBLE_URL_TEMPLATE, collection))
    response.raise_for_status()
    resp_body = response.json()
    for ids in resp_body:
        fetch_hubble_image(ids["id"])

