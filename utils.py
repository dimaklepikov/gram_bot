import requests

def file_downloader(url, name):
    response = requests.get(url)
    response.raise_for_status()
    with open('pictures/{}'.format(name), 'wb') as file:
        file.write(response.content)
