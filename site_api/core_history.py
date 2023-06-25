import os

from geopy import Nominatim

from database.core import crud
from site_api.utils.site_api_handler import SiteApiInterface

host_api = os.getenv('HOST_API')
api_key=os.getenv('RAPID_API_KEY')
db_read=crud.retrieve()
headers = {
    "X-RapidAPI-Key": api_key,
    "X-RapidAPI-Host": host_api
}

coords = Nominatim(user_agent='GetLoc')
getLoc = coords.geocode("SELECT history.place FROM history WHERE `id`=(SELECT max(id) FROM history)",language='ru')

url = "https://" + host_api

params = {"q":"Москва","dt":"<REQUIRED>","lang":"ru"}

site_api = SiteApiInterface

if __name__ == '__main__':
    site_api()
