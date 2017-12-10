"""This pulls the address points file from the open data portal"""

import io
import zipfile
import requests
import shapefile

RECORD_FIELDS = [
    'geo_id',
    'link',
    'maint_stag',
    'address',
    'lfname',
    'lonum',
    'lonumsuf',
    'hinum',
    'hinumsuf',
    'arc_side',
    'distance',
    'fcode',
    'fcode_des',
    'class',
    'name',
    'x',
    'y',
    'longitude',
    'latitude',
    'objectid',
    'mun_name',
    'ward_name']

KEY_FIELDS = ['address', 'lfname', 'name', 'mun_name']
BIG_LIST = 'big_list.txt'

def pull_shapefile():
    url = 'http://opendata.toronto.ca/gcc/address_points_wgs84.zip'
    resp = requests.get(url)
    zip_file = zipfile.ZipFile(io.BytesIO(resp.content))
    zip_file.extractall()

def record_to_tuple(record):
    return tuple([str(value) for key, value in zip(RECORD_FIELDS, record) if key in KEY_FIELDS])

def extract_shapefile():
    sf = shapefile.Reader('ADDRESS_POINT_WGS84')
    with open(BIG_LIST, 'w') as file_open:
        file_open.write('|'.join(KEY_FIELDS) + '\n')
        for record in sf.iterRecords():
            file_open.write('|'.join(record_to_tuple(record)) + '\n')

if __name__ == '__main__':
    #pull_shapefile()
    extract_shapefile()
