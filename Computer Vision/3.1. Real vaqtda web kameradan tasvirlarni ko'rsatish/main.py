import cv2

# kameradan o'qish
cap = cv2.VideoCapture(0)

while True:
    # ret - True - agar rasm(frame) mavjud bo'lsa, aks holda False
    ret, frame = cap.read()
    # rasmni ko'rsatish
    cv2.imshow("Freym", frame)

    # 1 ms kutadi, shu oraliqda foydalanuvchi biron
    # tugmani bossa, uni kodini qaytaradi
    key = cv2.waitKey(1)
    print(key)
    # Agar foydalanuvchi Esc ni bosgan bo'lsa, while tsiklidan chiqib ket
    if key == 27:
        break

# video kamerani bo'shatish
cap.release()
# barcha oynalarni yopish
cv2.destroyAllWindows()
