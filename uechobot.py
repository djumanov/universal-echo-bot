import requests
import json

TOKEN = '2052338771:AAHWqySU9KeCy3P_7i-2cLm3Fn78dLKG2RY'

# last update from telegram
def get_last_update() -> dict:
    '''this function returns last update as dictionary from telegram'''

    url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
    r = requests.get(url=url)
    if r.status_code == 200:
        last_update = r.json()['result'][-1]
        return last_update
    return False


# send to someone a message
def send_message(chat_id: int, text: str):
    '''this function sends message to someone'''

    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    data = dict([('chat_id', chat_id), ('text', text)])
    r = requests.post(url=url, data=data)


# send to someone a photo
def send_photo(chat_id: int, photo_id: str):
    '''this function sends photo to someone'''

    url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
    data = dict([('chat_id', chat_id), ('photo', photo_id)])
    r = requests.post(url=url, data=data)


# send to someone a document
def send_document(chat_id: int, file_id: str):
    '''this function sends file to someone'''
    
    url = f'https://api.telegram.org/bot{TOKEN}/sendDocument'
    data = dict([('chat_id', chat_id), ('document', file_id)])
    r = requests.post(url=url, data=data)


# send to someone an audio
def send_audio(chat_id: int, file_id: str):
    '''this function sends audio to someone'''
    
    url = f'https://api.telegram.org/bot{TOKEN}/sendAudio'
    data = dict([('chat_id', chat_id), ('audio', file_id)])
    r = requests.post(url=url, data=data)


# send to someone a video
def send_video(chat_id: int, file_id: str):
    '''this function sends video to someone'''
    
    url = f'https://api.telegram.org/bot{TOKEN}/sendVideo'
    data = dict([('chat_id', chat_id), ('video', file_id)])
    r = requests.post(url=url, data=data)


# send to someone a voice
def send_voice(chat_id: int, file_id: str):
    '''this function sends voice to someone'''
    
    url = f'https://api.telegram.org/bot{TOKEN}/sendVoice'
    data = dict([('chat_id', chat_id), ('voice', file_id)])
    r = requests.post(url=url, data=data)


# send to someone a location
def send_location(chat_id: int, latitude: float, longitude: float):
    '''this function sends location to someone'''
    
    url = f'https://api.telegram.org/bot{TOKEN}/sendLocation'
    data = dict([('chat_id', chat_id), ('latitude', latitude), ('longitude', longitude)])
    r = requests.post(url=url, data=data)


# send to someone a contect
def send_contact(chat_id: int, phone_number: str, first_name: str):
    '''this function sends contact to someone'''
    
    url = f'https://api.telegram.org/bot{TOKEN}/sendContact'
    data = dict([('chat_id', chat_id), ('phone_number', phone_number), ('first_name', first_name)])
    r = requests.post(url=url, data=data)


# send to someone a dice
def send_dice(chat_id: int, emoji: str):
    '''this function sends dice to someone'''     
    
    url = f'https://api.telegram.org/bot{TOKEN}/sendDice'
    data = dict([('chat_id', chat_id), ('emoji', emoji)])
    r = requests.post(url=url, data=data)


# send to someone a poll
def send_poll(chat_id: int, question: str, options: list):
    '''this function sends poll to someone'''  
    
    url = f'https://api.telegram.org/bot{TOKEN}/sendPoll'
    data = dict([('chat_id', chat_id), ('question', question), ('options', json.dumps(options))])
    r = requests.post(url=url, data=data)


# send to someone a collection of photos
def send_media_group(chat_id: int, files: list):
    '''this function sends file to someone'''
    
    url = f'https://api.telegram.org/bot{TOKEN}/sendMediaGroup'
    data = dict([('chat_id', chat_id), ('media', json.dumps(files))])
    r = requests.post(url=url, data=data)


# send to someone profile photos
def send_profile_photo(chat_id: int):
    '''this function sends profile photo'''

    url = f'https://api.telegram.org/bot{TOKEN}/getUserProfilePhotos'
    payload = {'user_id': chat_id}
    r = requests.get(url=url, params=payload)
    if r.status_code == 200:
        photos = r.json()['result']['photos']
        files = [{'media': item[-1]['file_id'], 'type': 'photo'} for item in photos]
        send_media_group(chat_id, files)


# send to someone a sticker 
def send_sticker(chat_id: int, sticker: str):
    '''this function sends a sticker'''

    url = f'https://api.telegram.org/bot{TOKEN}/sendSticker'
    payload = dict([('chat_id', chat_id), ('sticker', sticker)])
    r = requests.post(url=url, data=payload)
    


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
                            if text == '/glavni':
                                send_profile_photo(chat_id)
                            else:
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
                        elif 'poll' in message_type:
                            question = message['poll']['question']
                            options = [item['text'] for item in message['poll']['options']]
                            send_poll(chat_id, question, options)
                        elif 'sticker' in message_type:
                            sticker = message['sticker']['file_id']
                            send_sticker(chat_id, sticker)
                        elif 'media_group_id' in message_type:
                            files = [{'media': item['file_id'], 'type': 'photo'} for item in message['photo']]
                            send_media_group(chat_id, files)

                        last_update_id = curr_update_id

main()