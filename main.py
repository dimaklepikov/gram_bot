import requests
import os
from fetch_hubble import fetch_hubble_image, get_hubble_collection_pics, get_file_extetion
from fetch_spaceX import fetch_spacex_last_launch
from PIL import Image
from instabot import Bot
from PIL import ImageFile     #https://stackoverflow.com/questions/12984426/python-pil-ioerror-image-file-truncated-with-big-images
ImageFile.LOAD_TRUNCATED_IMAGES = True


if __name__ == '__main__':
    fetch_spacex_last_launch()
    get_file_extetion("https://imgsrc.hubblesite.org/hvi/uploads/image_file/image_attachment/1239/full_jpg.jpg")
    # fetch_hubble_image(1)
    get_hubble_collection_pics('wallpaper')
    
    for img in os.listdir(path='pictures'):
        image = Image.open('pictures/{}'.format(img))
        image.thumbnail((1080, 1080))
        rgb_im = image.convert('RGB')
        rgb_im.save('pictures/{}'.format(img))
        
    bot = Bot()
    bot.login(username="spacemongoose", password="aM2*ed9!mNHEY2qtE.*p")
    # bot.upload_photo('/home/dmitriy/Desktop/projects/Gram/pictures/hubble1.jpg.jpg')
    for img in os.listdir(path='pictures'):
        bot.upload_photo('pictures/{}'.format(img))