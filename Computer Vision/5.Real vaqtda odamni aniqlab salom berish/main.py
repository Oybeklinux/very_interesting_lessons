import os

import cv2
import pygame

from find_faces import FindFaces


def identify_faces(frame):
    face_locations, face_names = find_faces.detect_known_faces(frame)

    for location, name in zip(face_locations, face_names):
        # print(location, name)
        # tuple ni 4ta tushunarli bo'lgan o'zgaruvchiga oladi
        top, left, bottom, right = location
        # Ramkani chizadi
        cv2.rectangle(frame, (right, top), (left, bottom), (0, 0, 200), 4)
        # Ramka tepasiga ismini yozadi.
        cv2.putText(frame, name, (right + 20, top), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        if name != "Noma'lum" and name not in audio_played:
            audio_played[name] = True

            pygame.mixer.music.load(os.path.join(audios_path, f'{name}.mp3'))
            pygame.mixer.music.play()
            # playsound(os.path.join(audios_path, f'{name}.mp3'))


cap = cv2.VideoCapture('http://192.168.32.183:8080/video')
# cap = cv2.VideoCapture(0)

# mixerni sozlash
pygame.mixer.init()

# images katalogi yo'lini yasab oladi
current_dir = os.getcwd()

# rasm joylashgan yo'l
images_path = os.path.join(current_dir, "images")
# audio fayllar yo'li
audios_path = os.path.join(current_dir, "mp3")

# katalogdagi rasmlardan yuzlarni aniqlab sonlarga o'girib oladi
find_faces = FindFaces()
find_faces.load_encoding_images("images/")

audio_played = {}
while True:
    # ret - True - agar rasm(frame) mavjud bo'lsa, aks holda False
    ret, frame = cap.read()

    # Yuz lokatsiyasi va ismini oladi. Ismni fayl nomidan oladi
    if ret:
        identify_faces(frame)
        frame_c = cv2.resize(frame, (960, 540))  # Resize image

        # rasmni ko'rsatadi
        cv2.imshow("Freym", frame_c)

        # 1 ms kutadi, shu oraliqda foydalanuvchi biron
        # tugmani bossa, uni kodini qaytaradi
        key = cv2.waitKey(10)
        # Agar foydalanuvchi Esc ni bosgan bo'lsa, while tsiklidan chiqib ketadi
        if key == 27:
            break

# video kamerani bo'shatadi
cap.release()
# barcha oynalarni yopadi
cv2.destroyAllWindows()
