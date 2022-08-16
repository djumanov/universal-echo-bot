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


def send_message(chat_id, text):
    '''this function sends message to someone'''

    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    data = dict([('chat_id', chat_id), ('text', text)])
    r = requests.post(url=url, data=data)


def send_photo(chat_id, photo_id):
    '''this function sends photo to someone'''

    url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
    data = dict([('chat_id', chat_id), ('photo', photo_id)])
    r = requests.post(url=url, data=data)



def main():
    while True:
        last_update = get_last_update()
        if last_update:
            last_update_id = last_update['update_id']
            while True:
                curr_update = get_last_update()
                if curr_update:
                    curr_update_id = curr_update['update_id']
                    if last_update_id != curr_update_id:
                        message = curr_update['message']
                        chat_id = message['from']['id']
                        message_type = message.keys()
                        if 'text' in message_type:
                            text = message['text']
                            send_message(chat_id, text)
                        elif 'photo' in message_type:
                            photo_id = message['photo'][0]['file_id']
                            send_photo(chat_id, photo_id)
                        last_update_id = curr_update_id
            
main()