import requests
import os
import urllib.request

SPACEX_URL_TEMPLATE = 'https://api.spacexdata.com/v3/'

def file_download(url, name):
    urllib.request.urlretrieve(url, 'pictures/{}'.format(name))

def fetch_spacex_last_launch():
    response = requests.get('{}launches/latest'.format(SPACEX_URL_TEMPLATE))
    response.raise_for_status()
    resp_body = response.json()
    images_urls = resp_body["links"]["flickr_images"]
    
    for num, url in enumerate(images_urls):
        file_download(url, f"spacex{num}.jpg")