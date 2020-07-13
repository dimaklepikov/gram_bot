import requests
import os
import utils

SPACEX_URL_TEMPLATE = 'https://api.spacexdata.com/v3/'


def fetch_spacex_last_launch():
    response = requests.get('{}launches/latest'.format(SPACEX_URL_TEMPLATE))
    response.raise_for_status()
    resp_body = response.json()
    images_urls = resp_body["links"]["flickr_images"]
    
    for num, url in enumerate(images_urls):
        utils.get_file(url, f"spacex{num}.jpg")