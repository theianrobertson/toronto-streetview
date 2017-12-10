import logging
import csv
import random
import datetime

import requests
import data_pull
from twython import Twython
import config

IMAGE_URL = 'https://maps.googleapis.com/maps/api/streetview'
METADATA_URL = 'https://maps.googleapis.com/maps/api/streetview/metadata'
TEMP_IMAGE_NAME = 'to_upload.jpeg'

def get_image(address, filename=TEMP_IMAGE_NAME, size='800x800'):
    """Get an image with some metadata
    
    Parameters
    ----------
    address : str
        The address to pull
    filename : str
        Filename to save the file as
    size : str, optional
        Size of the image to request defaults to 800x800
    """
    params = {
        'size': size,
        'location': address,
        'key': config.API_KEY,
        'fov': 70
    }

    metadata = requests.get(METADATA_URL, params=params)
    if metadata.ok and metadata.json()['status'] == 'OK':
        resp = requests.get(IMAGE_URL, params=params)
        if resp.ok:
            with open(filename, 'wb') as file_open:
                file_open.write(resp.content)
        return metadata.json()['date']
    else:
        raise Exception('Bad metadata? {}'.format(address))

def grab_random_picture():
    """Pull a random picture, save it and return the status"""
    with open('big_list.txt') as file_open:
        for rows, _ in enumerate(file_open.readlines()):
            pass
    with open('big_list.txt') as csvfile:
        reader = csv.DictReader(csvfile, delimiter='|')
        for i, record in zip(range(random.randint(0, rows)), reader):
            pass
    address_lookup = '{} {}, Toronto ON Canada'.format(record['address'], record['lfname'])
    picture_date = get_image(address_lookup)
    mun = record['mun_name']
    if mun == 'former Toronto':
        mun = 'Toronto'
    status = '{} {}, {}'.format(
        record['address'], record['lfname'], mun)
    if len(record['name']) > 0:
        status = record['name'] + ', ' + status
    try:
        date = datetime.datetime.strptime(picture_date, '%Y-%m')
        status += ', {}'.format(date.strftime('%B %Y'))
    except:
        pass
    return status


def post_image(status, image_file=TEMP_IMAGE_NAME):
    """Send a post with image"""
    twitter = Twython(
        config.APP_KEY, config.APP_SECRET, config.OAUTH_TOKEN, config.OAUTH_TOKEN_SECRET)

    image = open(image_file, 'rb')
    response = twitter.upload_media(media=image)
    twitter.update_status(status=status, media_ids=[response['media_id']])
    print('Posted!')

if __name__ == '__main__':
    #for filename, address in [
    #    ('city.jpeg', '60 Queen St W, Toronto ON Canada'),
        #('craven.jpeg', '709 Craven Road, Toronto ON Canada'),
        #('yonge.jpeg', '5140 Yonge Street, Toronto ON Canada'),
        #('robina.jpeg', '45 Robina Avenue, Toronto ON Canada')
    #]:
    #    picture_date = get_image(address, filename)
    #    print('Address: {}, Date: {}'.format(address, picture_date))
    status = grab_random_picture()
    post_image(status)
