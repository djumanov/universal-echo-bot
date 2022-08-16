import requests

TOKEN = '2052462740:AAF5wRpqoXt2bm2a7JK5PlFPmcDLRGlajr0'

def get_last_update() -> dict:
    '''this function returns last update as dictionary from telegram'''

    url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
    r = requests.get(url=url)
    if r.status_code == 200:
        last_update = r.json()['result'][-1]
        return last_update
    return False

