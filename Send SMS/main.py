import json
import requests
from config import login, password

def get_status(reqiest_id):

    url = 'http://185.8.212.184/smsgateway/status/'

    send_data = {
        "login": login,
        "password": password,
        "data": json.dumps([{"request_id": str(reqiest_id)}])
    }
    try:
        result = requests.get(url=url, json=send_data)
        print(result.text)
    except Exception as error:
        print(error.args)



def send_sms(phone, text):
    url = 'http://185.8.212.184/smsgateway/'

    send_data = {
        "login": "Space",
        "password": "95TobJJuw929sKyZ590f",
        "data": json.dumps([{"phone": phone, "text": text}])
    }
    try:
        result = requests.post(url=url, json=send_data)
        print(result.text)
    except Exception as error:
        print(error.args)

text = """Bizning manzil:
Toshkent sh., Moʻminova ko'chasi bino 4\1, 100041. 
Aloqabank binosi, 16-qavat. 
Orientir: INHA universiteti

Kontaktlar:
Tel: +998 55-515-99-00

Telegram bot: @NextGenAcademy_bot

Telegram | Instagram | Veb-sahifa
ngen.uz
"""
phone1 = '998974251244'
phone2 = '998931676044'

send_sms(phone1, 'text')
# get_status(12810522)

# [{"recipient":998974251244,"text":"text","user_id":263,"date_received":1700043426,"message_id":81728619,"request_id":12810522,"client_ip":"194.93.24.168"}]