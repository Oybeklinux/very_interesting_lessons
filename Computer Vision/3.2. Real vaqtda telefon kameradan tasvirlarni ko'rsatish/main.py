import cv2

# kameradan o'qish
cap = cv2.VideoCapture('http://192.168.32.183:8080/video')

while True:
    # ret - True - agar rasm(frame) mavjud bo'lsa, aks holda False
    ret, frame = cap.read()
    # frame_c = cv2.resize(frame, (960, 540))  # Resize image

    # rasmni ko'rsatadi
    cv2.imshow("Freym", frame)

    # 1 ms kutadi, shu oraliqda foydalanuvchi biron
    # tugmani bossa, uni kodini qaytaradi
    key = cv2.waitKey(1)
    # Agar foydalanuvchi Esc ni bosgan bo'lsa, while tsiklidan chiqib ket
    if key == 27:
        break

# video kamerani bo'shatish
cap.release()
# barcha oynalarni yopish
cv2.destroyAllWindows()
