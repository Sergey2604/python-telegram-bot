from database.common.models import History, db
from database.core import crud
from site_api.core_current import site_api, url, headers, params
def to_work():
    db_wright = crud.create()
    db_read = crud.retrieve()

    fact_by_number = site_api.get_math_fact()
    curr_weather = site_api.get_curr_weather()

    # response = fact_by_number('GET', url, headers, 5, params, 5)
    # response = response.json()
    # data=[{'number':response.get('number'),'message':response.get('text')}]

    # db_wright(db,History,data)

    response = curr_weather('GET', url, headers, params, timeout=5)
    response = response.json()
    # print(response)
    def get_name_and_temp(dic:dict,search:str):
        for i,j in dic.items():
            if i==search:
                return j
            elif isinstance(j,dict) and j.__contains__(search):
                return get_name_and_temp(j,search)

    data=[{'place':get_name_and_temp(response,'name'),'message':get_name_and_temp(response,'temp_c')}]

    db_wright(db,History,data)

    retrieved=db_read(db,History,History.place,History.message)

    for elem in retrieved:
        print(elem.place,elem.message)

if __name__=='__main__':
    to_work()