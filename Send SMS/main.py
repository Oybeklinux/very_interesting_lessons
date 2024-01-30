# JSON format bilan ishlash uchun
import json
# internet bilan ishlash uchun
import requests
from config import login, password


# sms jo'natuvchi fubksiya
def send_sms(phone, text):
    # API manzil
    url = 'http://185.8.212.184/smsgateway/'

    # API ga jo'natiladigan ma'lumotlar
    send_data = {
        "login": login,
        "password": password,
        "data": json.dumps([{"phone": phone, "text": text}])
    }
    # xatolik yuz bersa ekranga chop qiladi
    try:
        # APIga murojaat va natijani olish
        result = requests.post(url=url, json=send_data)
        # natijani ekranga chop qilish
        print(result.text)
    except Exception as error:
        print(error.args)


text = "Assalomu alaykum, hurmatli talabalar!"
phone = '998974251244'
# funksiyani ishga tushirish
send_sms(phone, text)











def get_status(reqiest_id):

    url = 'http://185.8.212.184/smsgateway/status/'

    send_data = {
        "login": "Space",
        "password": "95TobJJuw929sKyZ590f",
        "data": json.dumps([{"request_id": str(reqiest_id)}])
    }
    try:
        result = requests.get(url=url, json=send_data)
        print(result.text)
    except Exception as error:
        print(error.args)

