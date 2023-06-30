import os

from site_api.utils.site_api_handler import SiteApiInterface

host_api = os.getenv('HOST_API')
api_key = os.getenv('RAPID_API_KEY')

headers = {
    "X-RapidAPI-Key": api_key,
    "X-RapidAPI-Host": host_api
}

url = "https://" + host_api

site_api = SiteApiInterface

if __name__ == '__main__':
    site_api()
