import requests
from pprint import pprint

TOKEN = '2034496504:AAFIqwOCqLq9aGlsguPaAq-W8eywOdEGOjA'

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


def send_document(chat_id, file_id):
    '''this function sends file to someone'''
    
    url = f'https://api.telegram.org/bot{TOKEN}/sendDocument'
    data = dict([('chat_id', chat_id), ('document', file_id)])
    r = requests.post(url=url, data=data)


def send_audio(chat_id, file_id):
    '''this function sends file to someone'''
    
    url = f'https://api.telegram.org/bot{TOKEN}/sendAudio'
    data = dict([('chat_id', chat_id), ('audio', file_id)])
    r = requests.post(url=url, data=data)


def send_video(chat_id, file_id):
    '''this function sends file to someone'''
    
    url = f'https://api.telegram.org/bot{TOKEN}/sendVideo'
    data = dict([('chat_id', chat_id), ('video', file_id)])
    r = requests.post(url=url, data=data)


def send_voice(chat_id, file_id):
    '''this function sends file to someone'''
    
    url = f'https://api.telegram.org/bot{TOKEN}/sendVoice'
    data = dict([('chat_id', chat_id), ('voice', file_id)])
    r = requests.post(url=url, data=data)


def send_location(chat_id, latitude, longitude):
    '''this function sends file to someone'''
    
    url = f'https://api.telegram.org/bot{TOKEN}/sendLocation'
    data = dict([('chat_id', chat_id), ('latitude', latitude), ('longitude', longitude)])
    r = requests.post(url=url, data=data)


def send_contact(chat_id, phone_number, first_name):
    '''this function sends file to someone'''
    
    url = f'https://api.telegram.org/bot{TOKEN}/sendContact'
    data = dict([('chat_id', chat_id), ('phone_number', phone_number), ('first_name', first_name)])
    r = requests.post(url=url, data=data)


def send_dice(chat_id, emoji):
    '''this function sends file to someone'''     
    
    url = f'https://api.telegram.org/bot{TOKEN}/sendDice'
    data = dict([('chat_id', chat_id), ('emoji', emoji)])
    r = requests.post(url=url, data=data)



def send_media_group(chat_id, files):
    '''this function sends file to someone'''
    
    url = f'https://api.telegram.org/bot{TOKEN}/sendMediaGroup'
    print('sending media group ...')
    data = dict([('chat_id', chat_id), ('media', files)])
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
                        elif 'photo' in message_type and 'media_group_id' not in message_type:
                            photo_id = message['photo'][0]['file_id']
                            send_photo(chat_id, photo_id)
                        elif 'document' in message_type:
                            file_id = message['document']['file_id']
                            send_document(chat_id, file_id)
                        elif 'audio' in message_type:
                            file_id = message['audio']['file_id']
                            send_audio(chat_id, file_id)
                        elif 'video' in message_type:
                            file_id = message['video']['file_id']
                            send_video(chat_id, file_id)
                        elif 'voice' in message_type:
                            file_id = message['voice']['file_id']
                            send_voice(chat_id, file_id)
                        elif 'location' in message_type:
                            x = message['location']['longitude']
                            y = message['location']['latitude']
                            send_location(chat_id, y, x)
                        elif 'contact' in message_type:
                            phone_number = message['contact']['phone_number']
                            first_name   = message['contact']['first_name']
                            send_contact(chat_id, phone_number, first_name)
                        elif 'dice' in message_type:
                            emoji = message['dice']['emoji']
                            send_dice(chat_id, emoji)
                        elif 'media_group_id' in message_type:
                            files = [{'media': item['file_id'], 'type': 'photo'} for item in message['photo']]
                            send_media_group(chat_id, files)

                        last_update_id = curr_update_id

main()