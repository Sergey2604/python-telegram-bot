from database.common.models import History, db
from database.core import crud
from site_api.core_current import site_api, url, headers


def to_work(user_id, message: str, date: str, format: str = 'low'):
    def get_temp(dic: dict, search: str):
        return dic['forecast']['forecastday'][0]['day'][search]

    db_wright = crud.create()
    db_read = crud.retrieve()

    history_weather = site_api.get_history_weather()

    params = {"q": message, "dt": date, "lang": "ru"}
    response = history_weather('GET', url, headers, params, timeout=5)
    response = response.json()
    data = None
    if format == 'low':
        data = [
            {"created_at": date, "user_id": str(user_id), "place": message, 'temp': get_temp(response, 'mintemp_c')}]
    elif format == 'high':
        data = [{"created_at": date, "user_id": user_id, "place": message, 'temp': get_temp(response, 'maxtemp_c')}]
    db_wright(db, History, data)

    retrieved = db_read(db, History, History.user_id, History.place, History.temp)

    for elem in retrieved:
        print(elem.user_id, elem.place, elem.temp)
