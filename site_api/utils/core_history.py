import os

from geopy import Nominatim

from site_api.utils.site_api_handler import SiteApiInterface

host_api = os.getenv('HOST_API')
api_key=os.getenv('RAPID_API_KEY')

headers = {
    "X-RapidAPI-Key": api_key,
    "X-RapidAPI-Host": host_api
}

coords = Nominatim(user_agent='GetLoc')
getLoc = coords.geocode("Москва",language='ru')

url = "https://" + host_api

params = {"q":"London","dt":"<REQUIRED>","lang":"ru"}

site_api = SiteApiInterface

if __name__ == '__main__':
    site_api()
