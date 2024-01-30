import requests
from bs4 import BeautifulSoup

# https://daryo.uz/2024/01/27/geosiyosiy-tahlil-eron-va-turiya-munosabati-urushga-hozirlanayotgan-aqsh
def malumotlarni_yuklab_olish(url):

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Ma'lumotlarni tahlil qilish va istalgan ma'lumotlarni olish
        # Masalan, agar 'p' tegi ichidagi ma'lumotlarni olishni istaysiz, quyidagi qatorni ishlatishingiz mumkin:
        # ma'lumotlar = soup.find_all('p')
        malumotlar = soup.find_all('p')  # Masalan, 'p' tegi ichidagi ma'lumotlarni olish

        for malumot in malumotlar:
            print(malumot.text)  # Ma'lumotni konsolga chiqarish
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")


if __name__ == "__main__":
    url = input("Yuklab olishni istagan veb-saytning manzilini kiriting: ")
    malumotlarni_yuklab_olish(url)
