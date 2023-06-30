from geopy import Nominatim

from database.common.models import History, db
from database.core import crud
from site_api.core_current import site_api, url, headers


def to_work(user_id, message: str):
    def get_name_and_temp(dic: dict, search: str):
        for i, j in dic.items():
            if i == search:
                return j
            elif isinstance(j, dict) and j.__contains__(search):
                return get_name_and_temp(j, search)

    db_wright = crud.create()
    db_read = crud.retrieve()

    curr_weather = site_api.get_curr_weather()

    coords = Nominatim(user_agent='GetLoc')
    getloc = coords.geocode(message, language='ru')
    print(getloc.latitude, getloc.longitude)
    params = {"q": "{0},{1}".format(getloc.latitude, getloc.longitude)}
    response = curr_weather('GET', url, headers, params, timeout=5)
    response = response.json()

    data = [{"user_id": user_id, "place": message, 'temp': get_name_and_temp(response, 'temp_c')}]
    db_wright(db, History, data)

    retrieved = db_read(db, History, History.user_id, History.place, History.temp)

    for elem in retrieved:
        print(elem.user_id, elem.place, elem.temp)
