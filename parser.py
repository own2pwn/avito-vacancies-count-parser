import requests
from time import sleep

HEADERS = {'User-Agent': 'AVITO 52.0 (iPad5,1; 11.3.1; en_RU)'}


def get_json(url: str):
    return requests.get(url, headers=HEADERS).json()


def get_locs() -> dict:
    locations = {621540: 'Вся Россия'}

    url = 'https://www.avito.ru/api/2/locations/top/children?includeRefs=1&key=7myrcPqWwSzInUCSvdwrtWcibz8pwaSNEMlRturi'
    j = get_json(url)
    for e in j:
        loc_id = int(e['id'])
        loc_name = e['names']['1']

        locations[loc_id] = loc_name

    return locations


def get_vacancies_count(by_loc_id: int) -> int:
    url = 'https://www.avito.ru/api/9/items?categoryId=110&countOnly=1&locationId={0}&sort=default&key=ZaeC8aidairahqu2Eeb1quee9einaeFieboocohX' \
        .format(by_loc_id)

    return int(get_json(url)['result']['count'])


def parse():
    locs = get_locs()
    for loc_id in locs:
        loc_name = locs[loc_id]
        c = get_vacancies_count(loc_id)

        print('{0} in {1}'.format(c, loc_name))
        sleep(1)


parse()
