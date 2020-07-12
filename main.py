import requests
import os
from fetch_hubble import fetch_hubble_image, get_hubble_collection_pics
from fetch_spaceX import fetch_spacex_last_launch
from PIL import Image
from instabot import Bot
from PIL import ImageFile
from dotenv import load_dotenv
ImageFile.LOAD_TRUNCATED_IMAGES = True


if __name__ == '__main__':
    fetch_spacex_last_launch()
    os.path.splitext("https://imgsrc.hubblesite.org/hvi/uploads/image_file/image_attachment/1239/full_jpg.jpg")
    get_hubble_collection_pics('wallpaper')
    load_dotenv(dotenv_path='.env', verbose=True)
    username = os.getenv('username')
    password = os.getenv('password')
    
    for img in os.listdir(path='pictures'):
        image = Image.open('pictures/{}'.format(img))
        image.thumbnail((1080, 1080))
        rgb_im = image.convert('RGB')
        rgb_im.save('pictures/{}'.format(img))
        
    bot = Bot()
    bot.login(username, password)
    for img in os.listdir(path='pictures'):
        bot.upload_photo('pictures/{}'.format(img))